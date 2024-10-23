"""Function for processing feature files from end-to-end."""

from __future__ import annotations

import logging
from pathlib import Path

from feefifofum.core.format import format_feature_file
from feefifofum.utils.file_utils import backup_file, read_file_lines, write_file_lines
from feefifofum.utils.log import generate_log_message

logger = logging.getLogger(__name__)


def process_files(file_paths: list[Path], backup: bool | None) -> tuple[int, int]:
    """
    Process files and return count of formatted and unchanged files.

    :param file_paths: List of feature file paths to process
    :param backup: Whether to backup original files before formatting (overwriting)
    :return: Counts of formatted and unchanged files
    """
    file_count = len(file_paths)
    changed_count, unchanged_count = 0, 0

    for index, file_path in enumerate(file_paths, 1):
        try:
            file_lines = read_file_lines(file_path)
        except (FileNotFoundError, PermissionError, UnicodeDecodeError, OSError) as e:
            read_error_message = generate_log_message(file_path=file_path, message=f'Failed reading from file: {e}')
            logger.error(read_error_message)
            continue

        formatted_file_lines = format_feature_file(file_lines)

        if file_lines == formatted_file_lines:
            debug_message = generate_log_message(
                file_path=file_path, message='Unchanged (skipped)', count=index, total_count=file_count
            )
            logger.debug(debug_message)
            unchanged_count += 1
            continue

        if backup:
            backup_file_path = file_path.with_suffix(file_path.suffix + '.bak')
            try:
                backup_file(file_path, backup_file_path)
                backup_message = generate_log_message(file_path=backup_file_path, message='Backed up')
                logger.debug(backup_message)
            except (FileNotFoundError, PermissionError, OSError) as e:
                backup_error_message = generate_log_message(
                    file_path=file_path, message=f'Failed backing up file: {e}', count=index, total_count=file_count
                )
                logger.error(backup_error_message)
                continue
        try:
            write_file_lines(formatted_file_lines, file_path)
        except (PermissionError, UnicodeEncodeError, OSError) as e:
            write_error_message = generate_log_message(file_path=file_path, message=f'Failed writing to file: {e}')
            logger.error(write_error_message)
            continue

        formatted_message = generate_log_message(
            file_path=file_path, message='Formatted', count=index, total_count=file_count
        )
        logger.debug(formatted_message)
        changed_count += 1

    return changed_count, unchanged_count
