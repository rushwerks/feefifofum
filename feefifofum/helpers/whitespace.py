from __future__ import annotations

from feefifofum.helpers.table import TABLE_SEPARATOR


INDENT_SIZE = 2

WHITESPACE_CONFIG: dict[str, tuple[int, int]] = {
    # 'Keyword': (Newline amount, indent amount)
    'Feature': (0, 0),
    'Scenario': (2, 1),
    'Given': (1, 2),
    'When': (1, 2),
    'Then': (1, 2),
    'And': (1, 2),
    'But': (1, 2),
    TABLE_SEPARATOR: (0, 3),
}


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

        if leading_word in WHITESPACE_CONFIG or line.startswith(TABLE_SEPARATOR):  # TODO: Test
            newline, indent = WHITESPACE_CONFIG[leading_word]
            previous_leading_word_match = leading_word
        else:
            newline, indent = WHITESPACE_CONFIG.get(previous_leading_word_match, (0, 0))
            newline = 0  # Keep in same feature file block
            indent += 1  # Indent by one level

        spaced.extend('\n' * newline)  # Add newline characters before line
        spaced.append(' ' * indent * INDENT_SIZE + line)  # Add leading whitespace to line

    return spaced
