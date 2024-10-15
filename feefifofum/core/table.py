"""Functions for identifying and formatting tables in feature files."""

from __future__ import annotations

from feefifofum.core.constants import TABLE_LEFT_EDGE, TABLE_RIGHT_EDGE, TABLE_SEPARATOR, TABLE_SPACER


def identify_and_format_tables(file_lines: list[str]) -> list[str]:
    """
    Identify and format feature file tables.

    :param file_lines: Feature file content as list of strings
    :return: Feature file lines with formatted tables
    """
    tables = find_tables(file_lines)

    for start_index, table in tables.items() or {}:
        formatted_table = table_formatter(table)
        end_index = start_index + len(table)
        file_lines[start_index:end_index] = formatted_table

    return file_lines


def find_tables(file_lines: list[str]) -> dict[int, list[str]]:
    """
    Find and extract feature file tables.

    :param file_lines: Feature file content as list of strings
    :return: Mapping of table start index to table content
    """
    table_mapping = {}  # {start_index: table_content}
    table = []
    start_index = None

    for index, line in enumerate(file_lines):
        if line.startswith(TABLE_SEPARATOR):
            start_index = start_index or index
            table.append(line)
        else:
            # Append current table (if it exists) once non-table encountered
            _add_table_to_mapping(table, start_index, table_mapping)
            table = []
            start_index = None

    # Append the last table if it exists
    _add_table_to_mapping(table, start_index, table_mapping)

    return table_mapping


def table_formatter(table: list[str]) -> list[str]:
    """
    Format feature file table by consistently spacing columns.

    :param table: Table as list of strings (each list element is a row)
    :return: Formatted feature file table
    """
    # Remove first and last cells which are empty strings, after split is applied
    rows = [row.strip().split(TABLE_SEPARATOR)[1:-1] for row in table]
    trimmed_rows = [[cell.strip() for cell in row] for row in rows]

    columns = _transpose_nested_list(trimmed_rows)
    column_widths = [max(len(cell) for cell in column) for column in columns]

    spaced_columns = [
        [cell.ljust(column_width) for cell in column] for column, column_width in zip(columns, column_widths)
    ]

    rows = _transpose_nested_list(spaced_columns)

    formatted_table = [f'{TABLE_LEFT_EDGE}{TABLE_SPACER.join(row)}{TABLE_RIGHT_EDGE}' for row in rows]

    return formatted_table


def _transpose_nested_list(nested_list: list[list]) -> list[list]:
    """
    Transpose the rows/columns of a (2D) nested list.

    :param nested_list: Nested list
    :return: Transposed nested list
    """
    return [list(x) for x in zip(*nested_list)]


def _add_table_to_mapping(table: list[str], start_index: int | None, table_mapping: dict[int, list[str]]) -> None:
    """
    Add table to table mapping if it has content.

    :param table: Table as list of strings (each list element is a row)
    :param start_index: Starting index of table
    :param table_mapping: Mapping of table starting index to table content
    """
    if table and start_index:
        table_mapping[start_index] = table
