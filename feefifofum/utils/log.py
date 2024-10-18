"""Utility functions for logging."""

from __future__ import annotations

from typing import Any


def generate_progress_message(count: int | str, total_count: int | str, action: str, message: Any) -> str:
    """
    Generate progress message for debugging/verbose output.

    :param count: Count of current iteration (or '-')
    :param total_count: Total number of iterations (or '-')
    :param action: Action performed
    :param message: Message to log
    :return: Debugging progress message
    """
    return f'({count}/{total_count}) | {action} | {message}'
