"""Utility functions for logging."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def generate_log_message(file_path: Path, message: Any, count: int | str = '-', total_count: int | str = '-') -> str:
    """
    Generate progress message for debugging/verbose output.

    :param file_path: File path to log information on
    :param message: Message to log
    :param count: Count of current iteration
    :param total_count: Total number of iterations
    :return: Debugging progress message
    """
    return f'({count}/{total_count}) | {file_path} - {message}'
