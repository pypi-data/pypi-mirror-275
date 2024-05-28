
from typing import Sequence, Tuple, Union
from typing_extensions import TypeAlias


import os
import numpy as np


PathLike: TypeAlias = Union[str, os.PathLike]
array1D: TypeAlias = np.ndarray
array2D: TypeAlias = np.ndarray
array1Dmask: TypeAlias = np.ndarray
array2Dmask: TypeAlias = np.ndarray


DATA_SPAN: TypeAlias = Sequence[Tuple[int, int]]
"""(row, column) pairs for each span cells"""

DATA_SPANS: TypeAlias = Sequence[DATA_SPAN]
"""spans sequence"""


SPANS_ARRAY: TypeAlias = array2D
"""
Nx3 array where 1st column is the span index, 2nd -- rows, 3rd -- cols
"""

