# O(N2 Log(N))

import numpy as np
from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        _2d = np.array(grid)
        # Flatten using numpy.flatten()
        _1d = sorted(_2d.flatten())

        r, m = 0, 0  # Initialize variables for repeated and missing values
        seen = set()

        for i in range(n * n):
            if _1d[i] in seen:  # If a value is already seen, it's the repeated one
                r = _1d[i]
            else:
                seen.add(_1d[i])

        # Identify the missing value
        for i in range(1, n * n + 1):
            if i not in seen:
                m = i
                break

        # Convert numpy.int64 to native Python int before returning
        return [int(r), int(m)]
