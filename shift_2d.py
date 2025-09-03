class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        # Flatten the 2D grid into a 1D list
        flat_list = []
        for row in grid:
            for item in row:
                flat_list.append(item)

        # Calculate the actual number of shifts needed to avoid redundant loops
        total_elements = rows * cols
        k %= total_elements
        
        # Perform the shift on the flattened list
        shifted_flat_list = flat_list[-k:] + flat_list[:-k]

        # Initialize the new grid with the correct dimensions
        ans = [[0 for _ in range(cols)] for _ in range(rows)]

        # Refill the new grid using the shifted 1D list
        for i in range(rows):
            for j in range(cols):
                index = i * cols + j
                ans[i][j] = shifted_flat_list[index]
                
        return ans
        