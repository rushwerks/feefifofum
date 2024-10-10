"""Function for running feature file formatter."""

from __future__ import annotations

from feefifofum.core.table import identify_and_format_tables
from feefifofum.core.whitespace import format_whitespace, strip_whitespace

def format_feature_file(file_lines: list[str]) -> list[str]:
    """
    Format feature file content.

    :param file_lines: Feature file content as list of strings
    :return: Formatted feature file content
    """
    stripped = strip_whitespace(file_lines)  # Whitespace must be stripped prior to format functions
    formatted = stripped[:]

    formatted = identify_and_format_tables(formatted)
    formatted = format_whitespace(formatted)

    return formatted
