class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:


        rows = len(grid)
        cols = len(grid[0])
        total_ops = 0
        prev_values = grid[0][:]
        for i in range(1, rows):
            for j in range(cols):
                if grid[i][j] <= prev_values[j]:
                    ops = prev_values[j] + 1 - grid[i][j]
                    total_ops += ops
                    prev_values[j] = grid[i][j] + ops  
                else:
                    prev_values[j] = grid[i][j]

        return total_ops
        