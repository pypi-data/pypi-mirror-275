
from typing import List, Callable, Any
from typing_extensions import TypeAlias

from ..utils.aliases import array2D, array1Dmask, array2Dmask

from .cell import LTRB


DATA_TABLE: TypeAlias = List[List[Any]]
"""list of lists of str"""


CANDIDATES_MASK_CREATOR: TypeAlias = Callable[[array2D, LTRB], array1Dmask]
"""
function ( 
    left-top-right-bottom array for each cell (Nx4 array), 
    (left, top, right, bottom) value of the current cell
) -> bool mask where True means current cell neighbours

this result mask determines the cells to check their mergability with the current cell;
    the current cell can be included in this mask, but there is no sense to do it

this function is called many times so it is necessary to implement it to be as fast as possible
    and to not include too many false candidates
"""

CHECKED_MASK_CREATOR: TypeAlias = Callable[[array2D, CANDIDATES_MASK_CREATOR], array2Dmask]
"""
function (
    left-top-right-bottom array for each cell (Nx4 array),
    helper function to get cell neighbours (can be ignored in your own implementations)
) -> 2D mask (NxN) where True means to NOT CHECK this cells pairs in the algorithm 
        (like they are not neighbours and there is no sense to check them)

this function is called only one time and recommended to be implemented to be fast
"""


