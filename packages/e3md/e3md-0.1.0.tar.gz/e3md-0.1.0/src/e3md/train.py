# -*- coding: utf-8 -*-
import contextlib
import logging
import pathlib
import time
from typing import Dict, Optional, Tuple, Type

import clu.metrics
import hydra
from hydra.core import hydra_config
import jax
from jax import random
from jax.lib import xla_bridge
import jraph
import omegaconf
import tensorial
from tensorial import gcnn

from . import config, stats

_LOGGER = logging.getLogger(__name__)

GraphsData = Tuple[jraph.GraphsTuple]


@contextlib.contextmanager
def log_action_with_timing(action: str, log_level=logging.INFO):
    t0 = 0.0
    try:
        _LOGGER.log(log_level, "Starting %s", action)
        t0 = time.time()
        yield
    finally:
        dt = time.time() - t0
        _LOGGER.log(log_level, "Finished %s, took %.2f s", action, dt)


def _validate(schema, cfg: omegaconf.DictConfig):
    # First merge into the schema
    return omegaconf.OmegaConf.merge(schema, cfg)


def validate_inplace(cfg: omegaconf.DictConfig) -> omegaconf.DictConfig:
    # Validate configurations
    omegaconf.OmegaConf.update(
        cfg, "globals", _validate(omegaconf.OmegaConf.structured(config.Globals), cfg.globals)
    )
    omegaconf.OmegaConf.update(
        cfg, "training", _validate(omegaconf.OmegaConf.structured(config.Training), cfg.training)
    )


def train(cfg: omegaconf.DictConfig):
    validate_inplace(cfg)

    # Inform the user if an accelerator is being used
    _LOGGER.info("Using JAX backend: %s", xla_bridge.get_backend().platform)

    output_dir = pathlib.Path(hydra_config.HydraConfig.get().runtime.output_dir)

    # Load data
    with log_action_with_timing("loading dataset(s)"):
        datasets = hydra.utils.instantiate(cfg.training.datasets)

    # Set up the configuration based on stats from the training set
    with log_action_with_timing("calculating stats from data"):
        calculate_stats(cfg.from_data, datasets["training"])

    loaders = create_loaders(cfg.training, datasets)
    training_loader = loaders["training"]

    _LOGGER.info("Configuration (%s):\n%s", output_dir, omegaconf.OmegaConf.to_yaml(cfg))
    rng_key = random.PRNGKey(cfg.globals.rng_key)

    # Create model
    model = tensorial.config.create_module(cfg.model)
    params = model.init(rng_key, next(iter(training_loader))[0])
    # Create trainer
    trainer = create_trainer(cfg.training, model.apply, params, loaders)

    device = get_device(cfg.globals.get("device"))
    log_header = "epoch e-train e-valid f-train f-valid"
    log_msg = (
        "%(epoch)5i "
        "%(training_energy).5f "
        "%(validation_energy).5f "
        "%(training_forces_rmse).5f "
        "%(validation_forces_rmse).5f "
    )
    metrics_logging = tensorial.training.MetricsLogging(log_every=1, msg=log_msg, header=log_header)
    with jax.default_device(
        device
    ), trainer._events.listen_context(  # pylint: disable=protected-access
        metrics_logging
    ):
        trainer.train(
            min_epochs=cfg.training.get("min_epochs"),
            max_epochs=cfg.training.max_epochs,
        )


def get_device(value: Optional[str]):
    if value:
        parts = value.split(":")
        name = parts[0]
        number = 0 if len(parts) == 1 else parts[1]
        return jax.devices(name)[number]

    return None


def calculate_stats(from_data: omegaconf.DictConfig, training_data: GraphsData):
    # Set up the configuration based on stats from the training set
    training_data = jraph.batch(training_data)

    results = {}
    for stat_name in from_data.values():
        results[stat_name] = stats.stat_calculators[stat_name](training_data, results)

    # Update the configuration with the values we calculated
    for key, stat_name in from_data.items():
        value = results[stat_name]
        from_data[key] = value.tolist() if isinstance(value, jax.Array) else value

    del training_data


def create_trainer(
    training: omegaconf.DictConfig,
    model: tensorial.training.ModelT,
    model_params,
    loaders: Dict[str, tensorial.data.DataLoader],
):
    # Create the various objects we need from the configuration
    loss_fn = hydra.utils.instantiate(training.loss_fn, _convert_="object")
    optimiser = hydra.utils.instantiate(training.optimiser, _convert_="object")
    metrics = create_metrics(training.metrics) if "metrics" in training else None

    return tensorial.training.Trainer(
        model,
        model_params,
        optimiser,
        loss_fn,
        train_data=loaders["training"],
        validate_data=loaders.get("validation"),
        metrics=metrics,
        # jit=0
    )


def create_loaders(
    training: omegaconf.DictConfig, datasets: Dict[str, Tuple[jraph.GraphsTuple]]
) -> Dict[str, gcnn.data.GraphLoader]:
    loaders = {}

    # Precalculate a padding that will work for all the datasets.  Only shuffle the training
    paddings = [
        gcnn.data.GraphBatcher.calculate_padding(
            graphs, training.batch_size, with_shuffle=name == "training"
        )
        for name, graphs in datasets.items()
    ]
    max_padding = gcnn.data.max_padding(*paddings)

    for name, graphs in datasets.items():
        if name == "training":
            loader = gcnn.data.GraphLoader(
                graphs,
                None,
                batch_size=training.batch_size,
                shuffle=training.shuffle,
                pad=True,
                padding=max_padding,
            )
            if training.get("shuffle_every", 1) != 1:
                # Wrap the training in a caching loader so that we only shuffle every so often
                # (not every epoch)
                loader = tensorial.data.CachingLoader(loader, reset_every=training.shuffle_every)

        else:
            # For the validation set we cache the whole thing as it never gets shuffled
            loader = tuple(
                gcnn.data.GraphLoader(
                    graphs,
                    None,
                    batch_size=training.batch_size,
                    shuffle=False,
                    pad=True,
                    padding=max_padding,
                )
            )
        loaders[name] = loader

    return loaders


def create_metrics(metrics: omegaconf.DictConfig) -> Type[clu.metrics.Collection]:
    metrics = {name: hydra.utils.instantiate(metric) for name, metric in metrics.items()}
    return clu.metrics.Collection.create(**metrics)
