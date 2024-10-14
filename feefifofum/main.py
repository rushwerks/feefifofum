"""Main entry point for feature file formatter."""

from __future__ import annotations

import logging
from argparse import ArgumentParser
from pathlib import Path

from feefifofum import __version__
from feefifofum.core.format import format_feature_file
from feefifofum.utils.file_utils import get_file_paths, read_file_lines, write_file_lines

logging.basicConfig(level=logging.INFO, format='%(message)s')


def main() -> None:  # pragma: no cover
    """Run feature file formatter."""
    parser = ArgumentParser(description='Formats feature file')
    parser.add_argument(
        'paths',
        type=Path,
        nargs='+',
        help='Path to feature files and/or directories',
    )
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    parser.add_argument('--version', '-V', action='version', version=f'%(prog)s {__version__}')

    args = parser.parse_args()
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    file_paths = get_file_paths(args.paths, '.feature')
    file_count = len(file_paths)

    if not file_count:
        logging.warning('No feature file(s) found in specified path(s)')
        return

    for index, file_path in enumerate(file_paths, 1):
        file_lines = read_file_lines(file_path)
        formatted_file_lines = format_feature_file(file_lines)
        write_file_lines(formatted_file_lines, file_path)
        logging.debug(f'Formatted: {file_path} ({index}/{file_count})')

    logging.info(f'Formatted {file_count} file(s)')


if __name__ == '__main__':  # pragma: no cover
    main()
