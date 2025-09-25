class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        # i = 0
        m = 0
        ans = [0] * len(grid[0])
        for g in grid:
            # print(g)
            for i in range(len(g)):
                k = len(str(g[i]))  
                if k > ans[i]:
                    ans[i] = k
            i += 1
            # print(ans)
        return ans

        