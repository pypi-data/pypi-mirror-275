# -*- coding: utf-8 -*-
"""
This module exposes some commonly used metrics
"""
import functools
from typing import Type

import clu.metrics
from tensorial import gcnn
import tensorial.metrics

__all__ = (
    "energy_per_atom",
    "energy_per_atom_rmse",
    "energy_per_atom_mae",
    "forces",
    "forces_rmse",
    "loss_mean",
)


def energy_per_atom(metric="rmse") -> Type[clu.metrics.Metric]:
    return gcnn.metrics.graph_metric(
        tensorial.metric(metric),
        "labels.globals.energy",
        "predictions.globals.predicted_energy",
        mask=("globals", gcnn.keys.MASK),
        _per_node=True,
    )


def forces(metric="rmse") -> Type[clu.metrics.Metric]:
    return gcnn.metrics.graph_metric(
        tensorial.metric(metric),
        "labels.nodes.forces",
        "predictions.nodes.predicted_forces",
        mask=("nodes", gcnn.keys.MASK),
    )


# Define some common ones for ease of use
energy_per_atom_rmse = functools.partial(energy_per_atom, "rmse")
energy_per_atom_mae = functools.partial(energy_per_atom, "mae")
forces_rmse = functools.partial(forces, "rmse")
loss_mean = functools.partial(clu.metrics.Average.from_output, "loss")
