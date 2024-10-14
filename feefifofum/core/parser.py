"""Function for parsing CLI arguments."""

from argparse import ArgumentParser, Namespace
from pathlib import Path

from feefifofum import __version__


def parse_args() -> Namespace:
    """
    Set up argument parser and parse CLI arguments.

    :return: Namespace object holding parsed arguments
    """
    parser = ArgumentParser(description='Formats feature file')
    parser.add_argument(
        'paths',
        type=Path,
        nargs='+',
        help='Path to feature files and/or directories',
    )
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    parser.add_argument('--version', '-V', action='version', version=f'%(prog)s {__version__}')

    return parser.parse_args()
