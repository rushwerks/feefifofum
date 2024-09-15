from __future__ import annotations

from feefifofum.helpers.constants import INDENT_SIZE, TABLE_SEPARATOR, WHITESPACE_CONFIG


def strip_whitespace(file_lines: list[str]) -> list[str]:
    """
    Strip whitespace from each line and add newline character to end of each line.

    :param file_lines: Feature file content as list of strings
    :return: Stripped list of lines, ending with newline character
    """
    return [f'{line.strip()}\n' for line in file_lines if line.strip()]


def format_whitespace(file_lines: list[str]) -> list[str]:
    """
    Format feature file whitespace - newlines and indentation.

    :param file_lines: Feature file content as list of strings
    :return: List of lines with appropriate whitespaces
    """
    previous_leading_word_match = 'Feature'  # Assumes first line in file should be unindented
    spaced = []

    for line in file_lines:
        leading_word = line.split(maxsplit=1)[0].rstrip(':')

        if leading_word in WHITESPACE_CONFIG or line.startswith(TABLE_SEPARATOR):
            whitespace_key = leading_word if leading_word in WHITESPACE_CONFIG else TABLE_SEPARATOR
            newline, indent = WHITESPACE_CONFIG[whitespace_key]
            previous_leading_word_match = whitespace_key
        else:
            newline, indent = WHITESPACE_CONFIG.get(previous_leading_word_match, (0, 0))
            newline = 0  # Keep in same feature file block
            indent += 1  # Indent by one level

        spaced.extend('\n' * newline)  # Add newline characters before line
        spaced.append(' ' * indent * INDENT_SIZE + line)  # Add leading whitespace to line

    return spaced
