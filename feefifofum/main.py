"""Main entry point for feature file formatter."""

import logging

from feefifofum.core.format import format_feature_file
from feefifofum.core.parser import parse_args
from feefifofum.utils.file_utils import get_file_paths, read_file_lines, write_file_lines


def main() -> None:  # pragma: no cover
    """Run feature file formatter."""
    args = parse_args()

    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format='%(message)s')

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
