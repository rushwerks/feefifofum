"""Utility functions for working with files."""

from __future__ import annotations

import shutil
from pathlib import Path


def get_file_paths(input_paths: list[Path], file_extension: str) -> list[Path]:
    """
    Get list of file paths based on paths and specified file extension.

    :param paths: Path(s) to files or directories containing files
    :param file_extension: File extension filter
    """
    output_paths = set()

    for path in input_paths:
        if path.is_file() and path.suffix == file_extension:
            output_paths.add(path)
        elif path.is_dir():
            path_list = list(path.rglob(f'*{file_extension}'))
            output_paths.update(path_list)

    return sorted(output_paths)


def read_file_lines(file_path: Path) -> list[str]:  # pragma: no cover
    """
    Read file and returns content in a list with each line as an element.

    :param file_path: File path to read from
    :return: File content as a list with each line as an element
    """
    with open(file_path) as file:
        return file.readlines()


def write_file_lines(content: list[str], file_path: Path) -> None:  # pragma: no cover
    """
    Write file with content provided in a list with each line as an element.

    :param content: File content as a list with each line as an element
    :param file_path: File path to write to
    """
    with open(file_path, 'w') as file:
        file.writelines(content)


def backup_file(file_path: Path) -> Path:  # pragma: no cover
    """
    Create backup copy of file.

    :param file_path: File path to backup
    :return: File path of backed up file
    """
    backup_file_path = file_path.with_suffix(file_path.suffix + '.bak')
    shutil.copy2(file_path, backup_file_path)  # Try to preserve metadata
    return backup_file_path
