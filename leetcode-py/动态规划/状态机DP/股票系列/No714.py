from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[0][1] = -inf
        for i, p in enumerate(prices):
            dp[i + 1][0] = max(dp[i][0], dp[i][1] + p - fee)
            dp[i + 1][1] = max(dp[i][1], dp[i][0] - p)
        return dp[n][0]

