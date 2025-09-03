class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        f = []

        for i in grid:
            for j in i:
                f.append(j)

        for n in range(k):
            f.insert(0, f.pop(-1))
        ans = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans[i][j] = f.pop(0)

        return ans
        