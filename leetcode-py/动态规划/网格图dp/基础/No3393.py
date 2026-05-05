from typing import List


class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        MOD  = 10 ** 9 + 7
        mx = 0
        for row in grid:
            for x in row:
                mx = max(mx, x)
        
        l = 1 << mx.bit_length()
        if k >= l:
            return 0


        m, n = len(grid), len(grid[0])
        dp = [[[0] * l for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][1][0] = 1
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                for t in range(l):
                    dp[i + 1][j + 1][t] = (dp[i + 1][j][t ^ x] + dp[i][j + 1][t ^ x]) % MOD
        
        return dp[m][n][k]