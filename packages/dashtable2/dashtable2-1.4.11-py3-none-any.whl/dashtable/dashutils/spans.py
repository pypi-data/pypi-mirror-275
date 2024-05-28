
from typing import Optional

import numpy as np

from .aliases import DATA_SPANS, DATA_SPAN, SPANS_ARRAY


def convert_spans_to_array(spans: DATA_SPANS) -> SPANS_ARRAY:
    """
    >>> convert_spans_to_array([[(1, 2), (5, 6)], [(7, 8)], [(9, 9), (8, 8)]])
    array([[0, 1, 2],
           [0, 5, 6],
           [1, 7, 8],
           [2, 9, 9],
           [2, 8, 8]])
    """
    return np.array(
        [
            (i, r, c)
            for i, sps in enumerate(spans)
            for r, c in sps
        ]
    )


def get_span(spans: DATA_SPANS, row: int, column: int) -> Optional[DATA_SPAN]:
    """
    Gets the span containing the [row, column] pair

    Parameters
    ----------
    spans : list of lists of lists
        A list containing spans, which are lists of [row, column] pairs
        that define where a span is inside a table.
    row :
    column :

    Returns
    -------
    span : list of lists
        A span containing the [row, column] pair
    """
    p = (row, column)
    for sps in spans:
        if p in sps:
            return sps

    return None


def get_span_index(spans_arr: SPANS_ARRAY, row: int, column: int) -> Optional[int]:
    """
    returns the index of the span contains this (row, column) pair;
       works faster than get_span and must replace it in future

    Parameters
    ----------
    spans_arr: Nx3 array where 1st column is the span index, 2nd -- rows, 3rd -- cols
    row
    column

    Returns
    -------

    >>> sps = [[(1, 2), (5, 6)], [(7, 8)], [(9, 9), (8, 8)], [(6, 5), (5, 5)]]
    >>> sps_arr = convert_spans_to_array(sps)
    >>> assert get_span_index(sps_arr, 5, 5) == 3
    >>> assert get_span_index(sps_arr, 5, 6) == 0
    >>> assert get_span_index(sps_arr, 7, 8) == 1
    >>> assert get_span_index(sps_arr, 5, 15) is None
    """
    mask = (spans_arr[:, 1] == row) & (spans_arr[:, 2] == column)
    indexes = spans_arr[mask]
    if indexes.size:
        return indexes[0, 0].item()
    return None


def get_longest_line_length(text: str):
    """Get the length longest line in a paragraph"""
    lines = text.split("\n")
    length = 0

    for i in range(len(lines)):
        if len(lines[i]) > length:
            length = len(lines[i])

    return length


def get_span_char_height(span: DATA_SPAN, row_heights):
    """
    Get the height of a span in the number of newlines it fills.

    Parameters
    ----------
    span : list of list of int
        A list of [row, column] pairs that make up the span
    row_heights : list of int
        A list of the number of newlines for each row in the table

    Returns
    -------
    total_height : int
        The height of the span in number of newlines
    """
    start_row = span[0][0]
    row_count = get_span_row_count(span)
    total_height = 0

    for i in range(start_row, start_row + row_count):
        total_height += row_heights[i]
    total_height += row_count - 1

    return total_height


def get_span_char_width(span: DATA_SPAN, column_widths):
    """
    Sum the widths of the columns that make up the span, plus the extra.

    Parameters
    ----------
    span : list of lists of int
        list of [row, column] pairs that make up the span
    column_widths : list of int
        The widths of the columns that make up the table

    Returns
    -------
    total_width : int
        The total width of the span
    """

    start_column = span[0][1]
    column_count = get_span_column_count(span)
    total_width = 0

    for i in range(start_column, start_column + column_count):
        total_width += column_widths[i]

    total_width += column_count - 1

    return total_width


def get_span_column_count(span: DATA_SPAN):
    """
    Find the length of a colspan.

    Parameters
    ----------
    span : list of lists of int
        The [row, column] pairs that make up the span

    Returns
    -------
    columns : int
        The number of columns included in the span

    Example
    -------
    Consider this table::

        +------+------------------+
        | foo  | bar              |
        +------+--------+---------+
        | spam | goblet | berries |
        +------+--------+---------+

    ::

        >>> span = [[0, 1], [0, 2]]
        >>> print(get_span_column_count(span))
        2
    """
    return len(
        {c for _, c in span}
    )


def get_span_row_count(span: DATA_SPAN):
    """
    Gets the number of rows included in a span

    Parameters
    ----------
    span : list of lists of int
        The [row, column] pairs that make up the span

    Returns
    -------
    rows : int
        The number of rows included in the span

    Example
    -------
    Consider this table::

        +--------+-----+
        | foo    | bar |
        +--------+     |
        | spam   |     |
        +--------+     |
        | goblet |     |
        +--------+-----+

    ::

        >>> span = [[0, 1], [1, 1], [2, 1]]
        >>> print(get_span_row_count(span))
        3
    """
    return len(
        {r for r, _ in span}
    )
