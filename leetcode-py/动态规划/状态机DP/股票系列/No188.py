from functools import cache
from math import inf
from typing import List

# 定义 dfs(i,j,0) 表示到第i天结束时还剩下至多 j 笔交易,未持有股票的最大利润
# 定义 dfs(i,j,1) 表示到第i天结束时还剩下至多 j 笔交易，持有股票的最大利润
class Solution:
    # dfs
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i: int, j: int , hold: int):
            if i < 0:
                return -inf if hold else 0
            if j > k:
                return -inf
            if hold:
                return max(dfs(i - 1, j, True), dfs(i - 1, j, False) - prices[i])
            return max(dfs(i - 1, j, False), dfs(i - 1, j + 1, True) + prices[i])

        return dfs(n - 1, 0, False)  # 255ms
    
class Solution:
    # dfs
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i: int, j: int , hold: int):
            if j > k:
                return -inf
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i - 1, j, True), dfs(i - 1, j + 1, False) - prices[i])
            return max(dfs(i - 1, j, False), dfs(i - 1, j, True) + prices[i])

        return dfs(n - 1, 0, False)

# 定义 dfs(i,j,0) 表示到第i天结束时完成至多 j 笔交易, 未持有股票的最大利润
# 定义 dfs(i;j,1) 表示到第i天结束时完成至多 j 笔交易，持有股票的最大利润
class Solution:
    # dfs
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int, hold: bool) -> int:
            if j < 0:
                return -inf
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i - 1, j, True), dfs(i - 1, j, False) - prices[i])
            return max(dfs(i - 1, j, False), dfs(i - 1, j - 1, True) + prices[i])
        return dfs(n - 1, k, False) # 243ms
    

class Solution:
    # 递推
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-inf] * 2 for _ in range(k + 2)] for _ in range(n + 1)]
        for j in range(1, k + 2):
            dp[0][j][0] = 0
        for i, p in enumerate(prices):
            for j in range(1, k + 2):
                dp[i + 1][j][0] = max(dp[i][j][0], dp[i][j - 1][1] + p)
                dp[i + 1][j][1] = max(dp[i][j][1], dp[i][j][0] - p)
        return dp[n][-1][0] # 115ms


class Solution:
    # 递推 + 空间优化
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-inf] * 2 for _ in range(k + 2)]
        for j in range(1, k + 2):
            dp[j][0] = 0
        for i, p in enumerate(prices):
            for j in range(1, k + 2):
                dp[j][1] = max(dp[j][1], dp[j][0] - p)
                dp[j][0] = max(dp[j][0], dp[j - 1][1] + p)
        return dp[-1][0]    ### 虽然能过，但是是错误的
        # 当处理到 j 时，j-1 已经在本轮循环中处理过了
        # 所以 dp[j-1][1] 已经是今天更新后的值
        # 但我们需要的是前一天的值
    
class Solution:
    # 递推 + 空间优化
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-inf] * 2 for _ in range(k + 2)]
        for j in range(1, k + 2):
            dp[j][0] = 0
        for i, p in enumerate(prices):
            for j in range(k + 1, 0, -1):
                dp[j][1] = max(dp[j][1], dp[j][0] - p)
                dp[j][0] = max(dp[j][0], dp[j - 1][1] + p)
        return dp[-1][0]    # 59ms