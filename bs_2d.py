# O(N*M)

import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return target in np.array(matrix).flatten()