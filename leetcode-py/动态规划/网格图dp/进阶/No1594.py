from math import inf
from typing import List

# 前置题目 No64
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 1_000_000_007
        m, n = len(grid), len(grid[0])
        dp = [[[1, 1] for _ in range(n + 1)] for _ in range(m + 1)]

        for i, row in enumerate(grid, start=1):
            for j, x in enumerate(row, start= 1):
                MIN, MAX = inf, -inf
                
                mn1, mx1 = dp[i][j - 1]
                mn2, mx2 = dp[i - 1][j]
                MIN = min(mn1 * x, mx1 * x, mn2 * x, mx2 * x)
                MAX = max(mn1 * x, mx1 * x, mn2 * x, mx2 * x)

                dp[i][j] = [MIN, MAX]

        ans = dp[m][n][1]
        return -1 if ans < 0 else ans % MOD # 错误
    

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 1_000_000_007
        m, n = len(grid), len(grid[0])
        
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
        dp[0][0] = [grid[0][0], grid[0][0]]
        for i in range(1, m):
            val = dp[i-1][0][0] * grid[i][0]
            dp[i][0] = [val, val]
        for j in range(1, n):
            val = dp[0][j-1][0] * grid[0][j]
            dp[0][j] = [val, val]

        for i in range(1, m):
            for j in range(1, n):
                x = grid[i][j]
                candidates = (
                    dp[i-1][j][0] * x, dp[i-1][j][1] * x,
                    dp[i][j-1][0] * x, dp[i][j-1][1] * x
                )
                dp[i][j] = [min(candidates), max(candidates)]

        ans = dp[m-1][n-1][1]
        return ans % MOD if ans >= 0 else -1