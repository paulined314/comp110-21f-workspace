"""Utility Functions."""

__author__ = "740490549"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows os a CSV inta a table."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV file
    csv_reader = DictReader(file_handle)

    # Read each rose of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produces a list[str] of all calues in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-orientated table to a column-orientated table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(a: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Head."""
    result: dict[str, list[str]] = {}
    if N >= len(a):
        for key in a:
            result[key] = []
            i: int = 0
            while i < len(a):
                result[key].append(a[key][i])
                i += 1
    else: 
        for key in a:
            result[key] = []
            counter: int = 0
            while counter < N:
                result[key].append(a[key][counter])
                counter += 1
    return result


def select(a: dict[str, list[str]], b: list[str]) -> dict[str, list[str]]:
    """Select."""
    result: dict[str, list[str]] = {}
    for key in b:
        result[key] = a[key]
    return result


def concat(a: dict[str, list[str]], b: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concat."""
    result: dict[str, list[str]] = {}
    for key in a:
        result[key] = a[key]
    for key in b:
        if key in result:
            i: int = 0
            while i < len(b[key]):
                result[key].append(b[key][i])
                i += 1
        else: 
            result[key] = b[key]
    return result
