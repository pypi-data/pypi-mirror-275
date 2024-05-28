
from typing import List, Dict, Tuple, Callable
from typing_extensions import TypeAlias

from collections import defaultdict

import numpy as np

from .aliases import CANDIDATES_MASK_CREATOR, CHECKED_MASK_CREATOR

from ..dashutils.aliases import array1Dmask, array2D, array2Dmask
from ..exceptions import NonMergableException

from .cell import Cell, LTRB
from .cell import get_merge_direction
from .cell import merge_cells


#region UTILS

def _get_empty_mask(size: int) -> array2Dmask:
    return np.zeros((size, size), dtype=bool)


def _get_diag_mask(size: int) -> array2Dmask:
    return np.diag(np.ones(size, dtype=bool))


def get_candidates_mask_v1(boxes: array2D, ltrb: LTRB) -> array1Dmask:
    """
    simplest candidates filter,
        does not exclude the cell itself and the most of the cells from the same row and same column

    Parameters
    ----------
    boxes
    ltrb

    Returns
    -------

    """
    l, t, r, b = ltrb
    candidates_mask = (
        (
            (boxes[:, 0] == l) & (boxes[:, 2] == r)
        ) | (
            (boxes[:, 1] == t) & (boxes[:, 3] == b)
        )
    )
    return candidates_mask


def get_candidates_mask_v2(boxes: array2D, ltrb: LTRB) -> array1Dmask:
    """
    comparing with v1, extremely filters candidates but works 2-times slower and therefore
        speeds up `merge_all_cells` by only 10%

    it is highly recommended to implement this logic using Cython or Numba

    Parameters
    ----------
    boxes
    ltrb

    Returns
    -------

    """
    l, t, r, b = ltrb
    candidates_mask = (
        (
            (boxes[:, 0] == l) & (boxes[:, 2] == r) & (
                (boxes[:, 1] == b) | (boxes[:, 3] == t)
            )
        ) | (
            (boxes[:, 1] == t) & (boxes[:, 3] == b) & (
                (boxes[:, 0] == r) | (boxes[:, 2] == l)
            )
        )
    )
    return candidates_mask


def get_checked_mask_v1(
    boxes: array2D,
    candidates_mask_creator: CANDIDATES_MASK_CREATOR = get_candidates_mask_v2
) -> array2Dmask:
    """
    simplest implementation

    Parameters
    ----------
    boxes
    candidates_mask_creator

    Returns
    -------

    """
    checked = _get_empty_mask(boxes.shape[0])
    """mask for caching that the cells pair must be checked or not"""

    for i, ltrb in enumerate(boxes):
        candidates_mask = candidates_mask_creator(boxes, ltrb)
        """
        mask of cells which may be the neighbours because of simplest criteria part

        other cells definitely cannot be neighbours and therefore must be excepted for speed up
        """
        neg = ~candidates_mask
        checked[i, neg] = True
        checked[neg, i] = True

    return checked


def get_checked_mask_v2(
    boxes: array2D,
    candidates_mask_creator: CANDIDATES_MASK_CREATOR = get_candidates_mask_v2
) -> array2Dmask:
    """
    simplest implementation

    Parameters
    ----------
    boxes
    candidates_mask_creator

    Returns
    -------

    """
    checked = _get_diag_mask(boxes.shape[0])
    """mask for caching that the cells pair must be checked or not"""

    for i, ltrb in enumerate(boxes[:-1], 1):
        candidates_mask = candidates_mask_creator(boxes[i:], ltrb)
        """
        mask of cells which may be the neighbours because of simplest criteria part

        other cells definitely cannot be neighbours and therefore must be excepted for speed up
        """
        neg = i + np.where(~candidates_mask)[0]
        checked[i - 1, neg] = True
        checked[neg, i - 1] = True

    return checked

#endregion


def merge_all_cells_v1(cells: List[Cell]) -> str:
    """
    Loop through list of cells and piece them together one by one

    Parameters
    ----------
    cells : list of dashtable.data2rst.Cell

    Returns
    -------
    grid_table : str
        The final grid table
    """

    checked = _get_empty_mask(len(cells))

    current = 0

    while len(cells) > 1:
        compared = 0
        c1 = cells[current]

        while compared < len(cells):
            c2 = cells[compared]

            merge_direction = get_merge_direction(c1, c2)
            if merge_direction:

                merge_cells(c1, c2, merge_direction)

                if current > compared:
                    current -= 1

                cells.pop(compared)

                checked = _get_empty_mask(len(cells))

            else:
                if checked[current, compared]:  # already checked
                    if checked.all():  # if all combinations checked -- raise infinite loop error
                        raise NonMergableException('current cells cannot be merged due to too complicated structure')

                checked[current, compared] = True
                compared += 1

        current += 1

        if current >= len(cells):
            current = 0

    return cells[0].text


# @profile
def merge_all_cells(
    cells: List[Cell],
    candidates_mask_creator: CANDIDATES_MASK_CREATOR = get_candidates_mask_v2,
    checked_mask_creator: CHECKED_MASK_CREATOR = get_checked_mask_v2
) -> str:
    """
    Loop through list of cells and piece them together one by one

    Parameters
    ----------
    cells : list of dashtable.data2rst.Cell
    candidates_mask_creator:
    checked_mask_creator:

    Returns
    -------
    grid_table : str
        The final grid table

    Notes
    -------
        this is the highly optimized version of `merge_all_cells_v1` which tries to minimize repeated calculations;
    """

    if len(cells) == 1:
        return cells[0].text

    #region PREPROCESSING

    init_cells = count_cells = len(cells)

    checked_available_mask = np.ones(count_cells, dtype=bool)
    """
    mask of the still available indexes (of rows/cols)
    
    it's more performant to use this new indexing layer instead of frequent rows/cols deletions with full copying
    """

    checked_available_indexes = np.where(checked_available_mask)[0]
    """
    available indexes (mask derivative)
    
    used for translating current indexes to real
    """

    #
    #
    # create `checked` mask
    #   with disabling 90%+ of pairs which are definitely not neighbours
    #
    #
    ltrb_array: array2D = np.array([c.left_top_right_bottom for c in cells])
    """array of (left, top, right, bottom) values for each cell"""

    checked = checked_mask_creator(ltrb_array, candidates_mask_creator)
    """mask for caching that the cells pair must be checked or not"""

    count_to_check = checked.size - checked.sum()
    """
    count of pairs that still are not checked

    always equal to 
        checked.size - checked.sum()
    but much more performant than computing this value any time
    """

    #endregion

    #region MAIN LOOP

    current = 0
    """outer loop indexer"""

    current_real = 0
    """real (matrix) index for the `current`"""

    while count_cells > 1:
        compared = 0
        """inner loop indexer"""

        c1 = cells[current]

        while compared < count_cells:
            if checked[
                current_real,
                checked_available_indexes[compared]
            ]:  # already checked -- skip here to speed up calculations
                if count_to_check:  # not all items checked

                    #
                    # fast way to get next not checked pair using numpy
                    #   without intensive python loops
                    #
                    _nexts = np.where(~checked[current_real, checked_available_indexes[compared + 1:]])[0]
                    if not _nexts.size:  # stop loop in no next
                        break
                    shift = 1 + _nexts[0]

                    compared += shift  # increase indexer
                    continue
                #
                # seems like all items checked
                #
                if len(cells) == 1:
                    return cells[0].text
                else:
                    #
                    # otherwise: all combinations checked -- raise infinite loop error
                    #
                    raise NonMergableException('current cells cannot be merged due to too complicated structure')

            c2 = cells[compared]

            #
            # get merge direction of c1 according to c2
            #   note that this function is not symmetric and must be performed for (c1, c2) as well as (c2, c1)
            #
            merge_direction = get_merge_direction(c1, c2)
            if merge_direction:  # if must be merged

                merge_cells(c1, c2, merge_direction)  # perform merge

                #region update caches

                _index = current_real
                """real index in the global array"""

                # assert count_to_check == checked.size - checked.sum()

                ############################
                #
                # next code resets the checking caches of all pairs with c1
                #   because c1 is changed
                #
                # here count_to_check must be increased by slice.sum()
                #   because slice.sum() == count of checked from slice
                #       and all this checked must be forgotten
                #
                ############################

                count_to_check += checked[checked_available_indexes, _index].sum()
                checked[checked_available_indexes, _index] = False

                # assert count_to_check == checked.size - checked.sum()

                count_to_check += checked[_index, checked_available_indexes].sum()
                checked[_index, checked_available_indexes] = False

                # assert count_to_check == checked.size - checked.sum()

                #############################
                #
                # for fully False slices perform checked filling according to the simplest criteria
                #   to speed up
                #
                # here count_to_check must be decreased by new checks counts
                #
                #############################
                ltrb = c1.left_top_right_bottom
                ltrb_array[_index] = ltrb

                candidates_mask = candidates_mask_creator(ltrb_array, ltrb)
                neg = np.where(~candidates_mask)[0]

                count_to_check -= neg.size - checked[_index, neg].sum()
                checked[_index, neg] = True
                count_to_check -= neg.size - checked[neg, _index].sum()
                checked[neg, _index] = True

                ####################
                #
                #
                # remove second cell info from all data
                #
                #
                ####################

                cells.pop(compared)
                count_cells -= 1

                _index = checked_available_indexes[compared]

                #
                # force set all this cell pairs to checked
                #   and decrease count_to_check by count of not already checked pairs
                #

                count_to_check -= init_cells - checked[_index, :].sum()
                checked[_index, :] = True
                # assert count_to_check == checked.size - checked.sum()

                count_to_check -= init_cells - checked[:, _index].sum()
                checked[:, _index] = True
                # assert count_to_check == checked.size - checked.sum()

                #
                # update indexes caches
                #
                checked_available_mask[_index] = False
                checked_available_indexes = np.where(checked_available_mask)[0]

                # count_to_check = checked.size - checked.sum()

                #
                # shift current in this case
                #
                if current > compared:
                    current -= 1

                current_real = checked_available_indexes[current]

                #endregion

            else:  # no merge -- continue watching

                # set flag that this pair is checked
                checked[current_real, checked_available_indexes[compared]] = True
                count_to_check -= 1

                _nexts = np.where(~checked[current_real, checked_available_indexes[compared + 1:]])[0]
                if not _nexts.size:
                    break
                shift = 1 + _nexts[0]
                compared += shift

        current += 1
        if current >= count_cells:
            current = 0

        current_real = checked_available_indexes[current]

    #endregion

    return cells[0].text

# @profile
# def merge_all_cells(cells: List[Cell]) -> str:
#     """
#     Loop through list of cells and piece them together one by one
#
#     Parameters
#     ----------
#     cells : list of dashtable.data2rst.Cell
#
#     Returns
#     -------
#     grid_table : str
#         The final grid table
#     """
#
#     if len(cells) == 1:
#         return cells[0].text
#
#     #region INITIALS
#
#     prev_cells = {i: c for i, c in enumerate(cells)}
#     """{ cell 'index' -> cell }"""
#     prev_count = len(prev_cells)
#
#     index_to_ltrb: Dict[int, Tuple[int, int, int, int]] = {}
#     """{ cell index -> (left, top, right, bottom }"""
#
#     left_right_to_indexes: Dict[Tuple[int, int], List[int]] = defaultdict(list)
#     """
#     { (left, right) -> [ cells indexes ] }
#
#     used for fast caching
#     """
#
#     top_bottom_to_indexes: Dict[Tuple[int, int], List[int]] = defaultdict(list)
#     """{ (top, bottom) -> [cells indexes] }"""
#
#     #
#     # fill caches
#     #
#     for i, c in prev_cells.items():
#         l, t, r, b = c.left_top_right_bottom
#         index_to_ltrb[i] = (l, t, r, b)
#         left_right_to_indexes[(l, r)].append(i)
#         top_bottom_to_indexes[(t, b)].append(i)
#
#     #endregion
#
#     new_cells: Dict[int, Cell] = {}
#
#     while True:
#
#         if len(prev_cells) < 2:  # there are not enough cells in this storage -- migrate from another storage
#             if len(prev_cells) == 1:
#                 new_cells.update(prev_cells)
#
#             new_count = len(new_cells)
#             if new_count == 1:
#                 break
#             if new_count == prev_count:  # infinite loop started
#                 raise NonMergableException(
#                     'current cells cannot be merged due to too complicated structure'
#                 )
#             prev_cells = new_cells
#             prev_count = new_count
#             new_cells = {}
#
#         i1, c1 = prev_cells.popitem()
#
#         l, t, r, b = index_to_ltrb[i1]
#
#         while True:  # use this cell until it works
#             possible_neighbours = [
#                 i for i in left_right_to_indexes[(l, r)] + top_bottom_to_indexes[(t, b)]
#                 if i != i1
#             ]
#             if not possible_neighbours:
#                 new_cells[i1] = c1
#                 break
#
#             for i2 in possible_neighbours:  # try first mergable
#
#                 if i2 == i1:
#                     continue
#
#                 c2 = prev_cells.get(i2)
#                 if c2 is None:  # this pair is already checked
#                     continue
#
#                 merge_direction = get_merge_direction(c1, c2)
#                 if not merge_direction:  # check if swap works
#                     merge_direction = get_merge_direction(c2, c1)
#                     if merge_direction:  # perform swap to simplify next code
#                         c1, c2 = c2, c1
#
#                 if merge_direction:  # merge and update caches
#                     merge_cells(c1, c2, merge_direction)
#
#                     #
#                     # update caches
#                     #
#                     prev_cells.pop(i2)
#
#                     for i in (i1, i2):
#                         left, top, right, bottom = index_to_ltrb.pop(i)
#                         left_right_to_indexes[(left, right)].remove(i)
#                         top_bottom_to_indexes[(top, bottom)].remove(i)
#
#                     l, t, r, b = c1.left_top_right_bottom
#                     index_to_ltrb[i1] = l, t, r, b
#                     left_right_to_indexes[(l, r)].append(i1)
#                     top_bottom_to_indexes[(t, b)].append(i1)
#
#                     new_cells[i1] = c1
#
#                     break
#
#             else:  # cannot merge with any of neighbours -- just move to next
#                 new_cells[i1] = c1
#                 break
#
#
#     return new_cells.popitem()[1].text

