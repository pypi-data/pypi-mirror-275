
import numpy as np

from ..dashutils.aliases import DATA_SPANS
from .aliases import DATA_TABLE

# from ..dashutils import get_span


# def table_cells_2_spans(table, spans):
#     """
#     Converts the table to a list of spans, for consistency.
#
#     This method combines the table data with the span data into a
#     single, more consistent type. Any normal cell will become a span
#     of just 1 column and 1 row.
#
#     Parameters
#     ----------
#     table : list of lists of str
#     spans : list of lists of int
#
#     Returns
#     -------
#     table : list of lists of lists of int
#         As you can imagine, this is pretty confusing for a human which
#         is why data2rst accepts table data and span data separately.
#     """
#     new_spans = []
#     for row in range(len(table)):
#         for column in range(len(table[row])):
#             span = get_span(spans, row, column)
#
#             if not span:
#                 new_spans.append([(row, column)])
#
#     new_spans.extend(spans)
#     new_spans = sorted(new_spans)
#
#     return new_spans

def table_cells_2_spans(table: DATA_TABLE, spans: DATA_SPANS) -> DATA_SPANS:
    """
    Converts the table to a list of spans, for consistency.

    This method combines the table data with the span data into a
    single, more consistent type. Any normal cell will become a span
    of just 1 column and 1 row.

    Parameters
    ----------
    table : list of lists of str
    spans : list of lists of int

    Returns
    -------
    table : list of lists of lists of int
        As you can imagine, this is pretty confusing for a human which
        is why data2rst accepts table data and span data separately.
    """

    total_rows = len(table)
    total_cols = len(table[0])
    table_index_to_span_index = np.ones((1 + total_rows, 1 + total_cols), dtype=bool)
    for sps in spans:
        for r, c in sps:
            table_index_to_span_index[r, c] = False

    new_spans = [
        [(row, column)]
        for row in range(total_rows)
        for column in range(total_cols)
        if table_index_to_span_index[row, column]
    ]

    return sorted(new_spans + spans)


