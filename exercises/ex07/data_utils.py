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


def columar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-orientated table to a column-orientated table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result