class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0 

        m, n = len(grid), len(grid[0])

        def isMagicSqaure(grid,r,c):
            seen = [False] * 10

            for i in range(3):
                for j in range(3):
                    num = grid[r+i][c+j]
                    if num < 1 or num > 9:
                        return False
                    if seen[num]:
                        return False
                    seen[num] = True
            dia1 = (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2])
            dia2 = (grid[r+2][c] + grid[r+1][c+1] + grid[r][c+2])

            if dia1 != dia2:
                return False
            
            r1 = grid[r][c] + grid[r][c+1] + grid[r][c+2]
            r2 = grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2]
            r3 = grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2]

            if not (r1 == dia1 and r2 == dia1 and r3 == dia1):
                return False

            c1 = grid[r][c] + grid[r + 1][c] + grid[r + 2][c]
            c2 = (grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 2][c + 1])
            c3 = (grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2])

            if not (c1 == dia1 and c2 == dia1 and c3 == dia1):
                return False
            
            return True

        for r in range(m-2):
            for c in range(n-2):
                if isMagicSqaure(grid, r, c):
                    ans += 1
        
        
        
        return ans