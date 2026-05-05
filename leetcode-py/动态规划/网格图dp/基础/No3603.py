from math import inf
from typing import List


class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        dp = [[inf] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(waitCost):
            for j, x in enumerate(row):
                if i == 0 and j == 0:
                    dp[i + 1][j + 1] = 1
                    continue
                dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1]) + x + (i + 1) * (j + 1)
        
        return dp[-1][-1] - waitCost[-1][-1]




