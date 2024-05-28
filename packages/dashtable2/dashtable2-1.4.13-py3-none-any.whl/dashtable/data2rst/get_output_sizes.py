
import numpy as np

from .aliases import DATA_TABLE

from ..dashutils.aliases import DATA_SPANS
from ..dashutils.spans import get_longest_line_length, get_span_column_count, get_span_row_count


# @profile
def get_output_column_widths(table: DATA_TABLE, spans: DATA_SPANS):
    """
    Gets the widths of the columns of the output table

    Parameters
    ----------
    table : list of lists of str
        The table of rows of text
    spans : list of lists of int
        The [row, column] pairs of combined cells

    Returns
    -------
    widths : list of int
        The widths of each column in the output table
    """

    total_rows = len(table)
    total_cols = len(table[0])

    widths = [3 for _ in range(total_cols)]

    spans_column_counts = np.array([get_span_column_count(s) for s in spans])
    table_index_to_span_index = np.empty((1 + total_rows, 1 + total_cols), dtype=np.uint32)
    for i, sps in enumerate(spans):
        for r, c in sps:
            table_index_to_span_index[r, c] = i

    for row in range(total_rows):
        for column in range(total_cols):
            i = table_index_to_span_index[row, column]
            span = spans[i]
            column_count = spans_column_counts[i]

            if column_count == 1:
                text_row = span[0][0]
                text_column = span[0][1]

                text = table[text_row][text_column]

                length = get_longest_line_length(text)
                if length > widths[column]:
                    widths[column] = length

    for row in range(total_rows):
        for column in range(total_cols):
            i = table_index_to_span_index[row, column]
            span = spans[i]
            column_count = spans_column_counts[i]

            if column_count > 1:
                text_row = span[0][0]
                text_column = span[0][1]

                text = table[text_row][text_column]

                end_column = text_column + column_count

                available_space = sum(
                    widths[text_column:end_column])
                available_space += column_count - 1

                length = get_longest_line_length(text)

                while length > available_space:
                    for i in range(text_column, end_column):
                        widths[i] += 1

                        available_space = sum(
                            widths[text_column:end_column])

                        available_space += column_count - 1
                        if length <= available_space:
                            break
    return widths


def get_output_row_heights(table: DATA_TABLE, spans: DATA_SPANS):
    """
    Get the heights of the rows of the output table.

    Parameters
    ----------
    table : list of lists of str
    spans : list of lists of int

    Returns
    -------
    heights : list of int
        The heights of each row in the output table
    """
    total_rows = len(table)
    total_cols = len(table[0])

    heights = [-1 for _ in range(total_rows)]

    spans_row_counts = np.array([get_span_row_count(s) for s in spans])
    table_index_to_span_index = np.empty((1 + total_rows, 1 + total_cols), dtype=np.uint32)
    for i, sps in enumerate(spans):
        for r, c in sps:
            table_index_to_span_index[r, c] = i

    for row in range(total_rows):
        for column in range(total_cols):
            i = table_index_to_span_index[row, column]
            # span = spans[i]
            row_count = spans_row_counts[i]

            text = table[row][column]
            height = len(text.split('\n'))
            if row_count == 1 and height > heights[row]:
                heights[row] = height

    for row in range(total_rows):
        for column in range(total_cols):
            i = table_index_to_span_index[row, column]
            span = spans[i]
            row_count = spans_row_counts[i]

            if row_count > 1:
                text_row = span[0][0]
                text_column = span[0][1]

                end_row = text_row + row_count

                text = table[text_row][text_column]

                height = len(text.split('\n')) - (row_count - 1)

                add_row = 0
                while height > sum(heights[text_row:end_row]):
                    heights[text_row + add_row] += 1
                    if add_row + 1 < row_count:
                        add_row += 1
                    else:
                        add_row = 0
    return heights
