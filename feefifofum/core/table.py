"""Functions for identifying and formatting tables in feature files."""

from __future__ import annotations

from feefifofum.core.constants import TABLE_LEFT_EDGE, TABLE_RIGHT_EDGE, TABLE_SEPARATOR, TABLE_SPACER


def identify_and_format_tables(stripped_file_lines: list[str]) -> list[str]:
    """
    Identify and format feature file tables.

    :param file_lines: Feature file lines stripped of whitespace
    :return: Feature file lines with formatted tables
    """
    formatted = stripped_file_lines.copy()  # Avoid modifying list in place
    tables = find_tables(formatted)

    for start_index, table in (tables or {}).items():
        formatted_table = table_formatter(table)
        end_index = start_index + len(table)
        formatted[start_index:end_index] = formatted_table

    return formatted


def find_tables(file_lines: list[str]) -> dict[int, list[str]]:
    """
    Find and extract tables in feature file.

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
            # Add current table to mapping if it exists, once non-table character is encountered
            table_mapping.update({start_index: table} if table else {})
            table = []
            start_index = None

    # Add last table to mapping if it exists
    table_mapping.update({start_index: table} if table else {})

    return table_mapping


def table_formatter(table: list[str]) -> list[str]:
    """
    Format feature file table by stripping cell whitespace and consistently spacing columns.

    :param table: Table as list of strings (each list element is a row)
    :return: Formatted feature file table
    """
    rows = _split_table_into_rows(table)
    columns = _transpose_nested_list(rows)
    padded_columns = _pad_columns(columns)
    formatted_rows = _transpose_nested_list(padded_columns)
    formatted_table = _combine_rows_into_table(formatted_rows)
    return formatted_table


def _split_table_into_rows(table: list[str]) -> list[list[str]]:
    """
    Split table into list of rows and strip whitespace from each cell.

    :param table: Table represented as list of strings
    :return: List of rows represented as list of cells
    """
    # Remove first and last cells which are empty strings, after split is applied
    split_rows = [row.strip().split(TABLE_SEPARATOR)[1:-1] for row in table]
    return [[cell.strip() for cell in row] for row in split_rows]


def _transpose_nested_list(nested_list: list[list]) -> list[list]:
    """
    Transpose the rows/columns of a (2D) nested list.

    :param nested_list: Nested list
    :return: Transposed nested list
    """
    return [list(x) for x in zip(*nested_list)]


def _pad_columns(columns: list[list[str]]) -> list[list[str]]:
    """
    Pad each column to a consistent width.

    :param columns: List of columns represented as list of cells
    :return: Padded list of columns
    """
    column_widths = [max(len(cell) for cell in column) for column in columns]
    return [[cell.ljust(column_width) for cell in column] for column, column_width in zip(columns, column_widths)]


def _combine_rows_into_table(rows: list[list[str]]) -> list[str]:
    """
    Combine list of rows into a single table.

    :param rows: List of rows represented as list of cells
    :return: Table represented as list of strings
    """
    return [f'{TABLE_LEFT_EDGE}{TABLE_SPACER.join(row)}{TABLE_RIGHT_EDGE}' for row in rows]
