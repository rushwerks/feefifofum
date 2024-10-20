"""Main entry point for feature file formatter."""

from __future__ import annotations

import logging
from pathlib import Path

from feefifofum.core.format import format_feature_file
from feefifofum.core.parse import parse_args
from feefifofum.utils.file_utils import backup_file, get_file_paths, read_file_lines, write_file_lines
from feefifofum.utils.log import generate_progress_message


def main() -> None:  # pragma: no cover
    """Run feature file formatter."""
    args = parse_args()

    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format='%(message)s')

    file_paths = get_file_paths(input_paths=args.paths, file_extension='.feature')

    if not file_paths:
        logging.warning('No feature file(s) found in specified path(s)')
        return

    changed_count, unchanged_count = _process_files(file_paths=file_paths, backup=args.backup)

    if changed_count:
        logging.info(f'{changed_count} file(s) formatted')

    if unchanged_count:
        logging.info(f'{unchanged_count} file(s) unchanged')


def _process_files(file_paths: list[Path], *, backup: bool | None) -> tuple[int, int]:
    """
    Process files and return count of changed and unchanged files.

    :param file_paths: List of feature file paths to process
    :param backup: Whether to backup original files before formatting (overwriting)
    :return: Counts of formatted and unchanged files
    """
    file_count = len(file_paths)
    changed_count, unchanged_count = 0, 0

    for index, file_path in enumerate(file_paths, 1):
        file_lines = read_file_lines(file_path)
        formatted_file_lines = format_feature_file(file_lines)

        if file_lines == formatted_file_lines:
            logging.debug(generate_progress_message(index, file_count, 'unchanged', file_path))
            unchanged_count += 1
            continue

        if backup:
            backup_file_path = backup_file(file_path)
            logging.debug(generate_progress_message('-', '-', 'backed up', backup_file_path))

        write_file_lines(formatted_file_lines, file_path)
        logging.debug(generate_progress_message(index, file_count, 'formatted', file_path))
        changed_count += 1

    return changed_count, unchanged_count


if __name__ == '__main__':  # pragma: no cover
    main()
