from math import inf
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [inf] * (n + 1)
        dp[1] = 0
        for i in range(m):
            for j in range(n):
                x = grid[i][j]
                dp[j + 1] = min(dp[j + 1], dp[j]) + x
        return dp[-1]


