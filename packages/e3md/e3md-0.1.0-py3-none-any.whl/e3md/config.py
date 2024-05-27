# -*- coding: utf-8 -*-
import dataclasses
from typing import Any, Dict, List, Optional, Tuple, Union

from flax.training import orbax_utils
import flax.training.train_state
import omegaconf
import orbax.checkpoint
import tensorial

__all__ = 'load_module_state', 'Initialisable'

Config = Union[omegaconf.DictConfig, omegaconf.ListConfig]

MODULE_STATE = 'state'
MODULE_CONFIG = 'config'
TRAIN_STATE = 'train_state'


@dataclasses.dataclass
class FromData:
    n_elements: Optional[int]
    atomic_numbers: Optional[List[int]]
    avg_num_neighbours: Optional[float]


@dataclasses.dataclass
class Globals:
    r_max: float
    rng_key: int = 0
    device: Optional[str] = None


Initialisable = Dict


@dataclasses.dataclass
class Training:
    min_epochs: Optional[int]
    loss_fn: Initialisable
    optimiser: Initialisable
    metrics: Dict[str, Initialisable]
    datasets: Initialisable

    max_epochs: Optional[int] = tensorial.training.DEFAULT_MAX_EPOCHS
    batch_size: Optional[int] = 16
    shuffle: Optional[bool] = True
    shuffle_every: Optional[int] = 1


def create_train_checkpoint(train_state: flax.training.train_state.TrainState):
    return {
        TRAIN_STATE: train_state,
    }


def create_module_checkpoint(module_config: Config, module_state) -> Dict:
    return {
        MODULE_CONFIG: omegaconf.OmegaConf.to_container(module_config, resolve=True),
        MODULE_STATE: module_state,
    }


def save_module(path, module_config: Config, module_state):
    save_state = create_module_checkpoint(module_config, module_state)
    checkpointer = orbax.checkpoint.PyTreeCheckpointer()
    checkpointer.save(
        path,
        save_state,
        save_args=orbax_utils.save_args_from_target(save_state),
    )


def load_module_state(path) -> Tuple[Config, Any]:
    checkpointer = orbax.checkpoint.PyTreeCheckpointer()
    state = checkpointer.restore(path)
    return omegaconf.OmegaConf.create(state[MODULE_CONFIG]), state[MODULE_STATE]
