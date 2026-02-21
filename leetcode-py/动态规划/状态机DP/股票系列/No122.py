from functools import cache
from math import inf
from typing import List


class Solution:
    # 双指针
    def maxProfit(self, prices: List[int]) -> int:
        ans = pre = 0
        prices = prices + [-1]
        n = len(prices)
        for i in range(1, n):
            if prices[i] >= prices[i - 1]:
                continue
            else:
                ans += prices[i - 1] - prices[pre]
                pre = i
        return ans

class Solution:
    # 贪心
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                ans += prices[i] - prices[i - 1]
        return ans

# 双指针看重上升曲线的首尾， 而贪心则是逐过程


# 重头戏：DP

class Solution:
    # dfs
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int, hold: bool) -> int:
            if i < 0:   # 不允许退出时候还持有
                return -inf if hold else 0
            if hold:    # 此时持有时，上时刻未持有的状态买入 或 持有状态保持不变
                return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])
            # 此时未持有，上时刻持有的状态出售 或 未持有状态保持不变
            return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])
        return dfs(n - 1, False)
    

class Solution:
    # 递推
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[0][1] = -inf
        for i, p in enumerate(prices):
            dp[i + 1][0] = max(dp[i][0], dp[i][1] + p)
            dp[i + 1][1] = max(dp[i][1], dp[i][0] - p)
        return dp[n][0]

class Solution:
    # 递推
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-inf] * 2 for _ in range(n + 1)]
        dp[0][0] = 0
        for i, p in enumerate(prices):
            dp[i + 1][0] = max(dp[i][0], dp[i][1] + p)
            dp[i + 1][1] = max(dp[i][1], dp[i][0] - p)
        return dp[n][0]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f0, f1 = 0, -inf
        for p in prices:
            f0, f1 = max(f0, f1 + p), max(f1, f0 - p)
        return f0