
from typing import Sequence, Tuple
from typing_extensions import TypeAlias

from ..utils.aliases import array2D

DATA_SPAN: TypeAlias = Sequence[Tuple[int, int]]
"""(row, column) pairs for each span cells"""

DATA_SPANS: TypeAlias = Sequence[DATA_SPAN]
"""spans sequence"""

SPANS_ARRAY: TypeAlias = array2D
"""
Nx3 array where 1st column is the span index, 2nd -- rows, 3rd -- cols
"""

