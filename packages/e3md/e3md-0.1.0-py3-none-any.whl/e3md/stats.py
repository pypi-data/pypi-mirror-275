# -*- coding: utf-8 -*-
from typing import Dict, Sequence, Tuple

import jax
import jax.numpy as jnp
import jraph
from pytray import tree
from tensorial import gcnn

__all__ = ("estimate_species_contribution", "stat_calculators")


def estimate_species_contribution(
    graphs: jraph.GraphsTuple,
    value_field: str,
    type_field: str = ("nodes", gcnn.keys.SPECIES),
    type_map: Sequence[int] = None,
) -> Tuple[jax.Array, jax.Array]:
    """Estimates the contribution of the one hot encoded field to the final value

    :param graphs: a graphs tuple containing all the atomic structures
    :param value_field: the field containing the final values
    :param type_field: the field containing the type index of atomic species
    :return: the least squares contribution
    """
    graph_dict = graphs._asdict()
    value_field = gcnn.utils.path_from_str(value_field)
    type_field = gcnn.utils.path_from_str(type_field)
    num_nodes = graphs.n_node

    type_values = tree.get_by_path(graph_dict, type_field)
    if type_map is not None:
        # Transform the atomic numbers into from whatever they are to 0, 1, 2....
        vwhere = jax.vmap(lambda num: jnp.argwhere(num == type_map, size=1)[0])
        type_values = vwhere(type_values)[:, 0]

    num_classes = type_values.max().item() + 1  # Assume the types go 0,1,2...N
    one_hots = jax.nn.one_hot(type_values, num_classes)

    one_hot_field = ("type_one_hot",)
    tree.set_by_path(graphs.nodes, one_hot_field, one_hots)
    type_values = gcnn.reduce(graphs, ("nodes",) + one_hot_field, reduction="sum")

    # Predicting values
    values = tree.get_by_path(graph_dict, value_field)

    # Normalise by number of nodes
    type_values = jax.vmap(lambda numer, denom: numer / denom, (0, 0))(type_values, num_nodes)
    values = jax.vmap(lambda numer, denom: numer / denom, (0, 0))(values, num_nodes)

    contributions = jnp.linalg.lstsq(type_values, values)[0]
    estimates = type_values @ contributions
    stds = jnp.std(values - estimates)

    return contributions, stds


def energy_per_atom_lstsq(graphs: jraph.GraphsTuple, stats: Dict[str, jnp.ndarray]) -> jnp.ndarray:
    return estimate_species_contribution(
        graphs,
        value_field=("globals", "energy"),
        type_field=("nodes", gcnn.atomic.ATOMIC_NUMBERS),
        type_map=stats["all_atomic_numbers"],
    )[0]


stat_calculators = {
    "max_species": lambda graphs, _: jnp.unique(graphs.nodes[gcnn.atomic.ATOMIC_NUMBERS]).shape[0],
    "all_atomic_numbers": lambda graphs, _: jnp.unique(graphs.nodes[gcnn.atomic.ATOMIC_NUMBERS]),
    "avg_num_neighbours": lambda graphs, _: jnp.unique(graphs.senders, return_counts=True)[
        1
    ].mean(),
    "force_std": lambda graphs, _: graphs.nodes[gcnn.atomic.FORCES].std(),
    "energy_per_atom_lstsq": energy_per_atom_lstsq,
}
