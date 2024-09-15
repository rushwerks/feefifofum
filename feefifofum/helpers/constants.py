from __future__ import annotations

from typing import NamedTuple

# Table
TABLE_SEPARATOR = '|'
TABLE_SPACER = ' | '
TABLE_LEFT_EDGE = '| '
TABLE_RIGHT_EDGE = ' |\n'


# Whitespace
class Whitespace(NamedTuple):
    newline: int
    indent: int


WHITESPACE_CONFIG: dict[str, Whitespace] = {
    'Feature': Whitespace(0, 0),
    'Scenario': Whitespace(2, 1),
    'Given': Whitespace(1, 2),
    'When': Whitespace(1, 2),
    'Then': Whitespace(1, 2),
    'And': Whitespace(1, 2),
    'But': Whitespace(1, 2),
    TABLE_SEPARATOR: Whitespace(0, 3),
}

INDENT_SIZE = 2
