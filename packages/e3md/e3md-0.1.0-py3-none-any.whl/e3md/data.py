# -*- coding: utf-8 -*-
import functools
import numbers
import os
from typing import Dict, Sequence, Tuple

import ase.io
import jraph
from tensorial import gcnn
import tensorial.data

Datasets = Dict[str, gcnn.data.GraphLoader]


def load_datasets_ase(
    paths: Dict[str, os.PathLike],
    read_function=ase.io.read,
    limits: Dict[str, int] = None,
    **kwargs,
) -> Dict[str, Tuple[jraph.GraphsTuple]]:
    to_graph = functools.partial(gcnn.atomic.graph_from_ase, **kwargs)

    datasets = {}
    for name, path in paths.items():
        ase_structures = read_function(path, index=':')
        if name in limits:
            ase_structures = ase_structures[:limits[name]]

        datasets[name] = tuple(map(to_graph, ase_structures))

    return datasets


def load_datasets_ase_split(
    path: os.PathLike,
    splits: Dict[str, numbers.Number],
    read_function=ase.io.read,
    **kwargs,
) -> Dict[str, Tuple[jraph.GraphsTuple]]:
    to_graph = functools.partial(
        gcnn.atomic.graph_from_ase,
        **kwargs,
    )
    ase_structures = read_function(path, index=':')
    graphs = tuple(map(to_graph, ase_structures))
    total = len(graphs)
    split_total = sum(splits.values())

    datasets = {}
    num_taken = 0
    for name, split in splits.items():
        num = int(split / split_total * total)
        datasets[name] = graphs[num_taken:num_taken + num]

    return datasets


def create_batches(
    name: str, graphs: Sequence, batch_size: int, shuffle: bool
) -> gcnn.data.GraphLoader:
    if name == 'training':
        # Wrap the training in a caching loader so that we only shuffle every so often
        # (not every epoch)
        dataset = tensorial.data.CachingLoader(
            gcnn.data.GraphLoader(graphs, None, batch_size=batch_size, shuffle=shuffle, pad=True),
            reset_every=10,
        )
    else:
        # For the validation set we cache the whole thing as it never gets shuffled
        dataset = tuple(
            gcnn.data.GraphLoader(graphs, None, batch_size=batch_size, shuffle=False, pad=True)
        )

    return dataset
