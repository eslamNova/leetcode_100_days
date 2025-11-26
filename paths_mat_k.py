class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # Initialize first row DP
        prev = [[0] * k for _ in range(n)]
        start_r = grid[0][0] % k
        prev[0][start_r] = 1

        # Fill first row
        for j in range(1, n):
            v = grid[0][j]
            for r in range(k):
                new_r = (r + v) % k
                prev[j][new_r] = (prev[j][new_r] + prev[j-1][r]) % MOD

        # Fill remaining rows
        for i in range(1, m):
            curr = [[0] * k for _ in range(n)]
            for j in range(n):
                v = grid[i][j]
                for r in range(k):
                    new_r = (r + v) % k

                    # From top
                    curr[j][new_r] = (curr[j][new_r] + prev[j][r]) % MOD

                    # From left
                    if j > 0:
                        curr[j][new_r] = (curr[j][new_r] + curr[j-1][r]) % MOD

            prev = curr  # Move current row to previous

        # Answer: paths ending at bottom-right with remainder 0
        return prev[n-1][0]
        