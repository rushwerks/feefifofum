"""Main entry point for feature file formatter."""

from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path

from feefifofum.core.format import format_feature_file
from feefifofum.utils.file_utils import get_file_paths, read_file_lines, write_file_lines


def main() -> None:  # pragma: no cover
    """Run feature file formatter."""
    parser = ArgumentParser(description='Formats feature file')
    parser.add_argument(
        'paths',
        type=Path,
        nargs='+',
        help='Path to feature files and/or directories',
    )
    args = parser.parse_args()

    file_paths = get_file_paths(args.paths, '.feature')
    file_count = len(file_paths)

    if not file_count:
        print('No feature file(s) found in specified path(s)')
        return

    for index, file_path in enumerate(file_paths, 1):
        file_lines = read_file_lines(file_path)

        formatted_file_lines = format_feature_file(file_lines)

        write_file_lines(formatted_file_lines, file_path)

        print(f'Formatted: {file_path} ({index}/{file_count})')


if __name__ == '__main__':  # pragma: no cover
    main()
