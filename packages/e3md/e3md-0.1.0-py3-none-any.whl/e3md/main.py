# -*- coding: utf-8 -*-
"""Main CLI command"""
# pylint: disable=wrong-import-position, wrong-import-order
import os

# Make sure we don't pre allocate memory, this is just antisocial
os.environ['XLA_PYTHON_CLIENT_PREALLOCATE'] = 'false'

import argparse
import pathlib
import sys
from typing import Final

import hydra

from . import train

COMMAND: Final[str] = 'command'
TRAIN: Final[str] = 'train'
TRAIN_SCRIPT_DEFAULT: Final[str] = 'configs/default.yaml'


def main_cli():
    parser = argparse.ArgumentParser('e3md')
    commands = parser.add_subparsers(dest=COMMAND, required=True)

    # The 'train' command
    train_parser = commands.add_parser(TRAIN, help='Train a model')
    train_parser.add_argument(
        '-i',
        '--input',
        nargs='?',
        type=pathlib.Path,
        help='Training script',
        default=TRAIN_SCRIPT_DEFAULT,
    )

    # Parse the args
    args, _rest = parser.parse_known_args()

    if args.command == TRAIN:
        # Set the command line arguments to what remains so hydra can deal with it
        sys.argv = sys.argv[0:1] + _rest

        script_path = args.input
        train_fn = hydra.main(
            version_base='1.3',
            config_path=str(script_path.parent.absolute()),
            config_name=script_path.stem,
        )(train.train)
        train_fn()


if __name__ == '__main__':
    main_cli()
