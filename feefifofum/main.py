"""Main entry point for feature file formatter."""

from __future__ import annotations

import logging

from feefifofum.core.parse import parse_args
from feefifofum.core.process import process_files
from feefifofum.utils.file_utils import get_file_paths


def main() -> None:  # pragma: no cover
    """Run feature file formatter."""
    args = parse_args()

    _configure_logger(verbose=args.verbose)
    logger = logging.getLogger(__name__)

    file_paths = get_file_paths(input_paths=args.paths, file_extension='.feature')

    if not file_paths:
        logger.warning('No feature files found in specified path(s)')
        return

    changed_count, unchanged_count = process_files(file_paths=file_paths, backup=args.backup)

    if changed_count:
        logger.info(f'{changed_count} file(s) formatted')

    if unchanged_count:
        logger.info(f'{unchanged_count} file(s) unchanged')


def _configure_logger(verbose: bool | None) -> None:
    """
    Configure root logger.

    :param verbose: Verbose (debug) logging flag
    """
    log_level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=log_level, format='%(message)s')


if __name__ == '__main__':  # pragma: no cover
    main()
