from math import inf
from typing import List


# 至多 k 次
class Solution:
    # 递推 No188
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-inf] * 2 for _ in range(k + 2)] for _ in range(n + 1)]
        for j in range(1, k + 2):
            dp[0][j][0] = 0
        for i, p in enumerate(prices):
            for j in range(1, k + 2):
                dp[i + 1][j][0] = max(dp[i][j][0], dp[i][j - 1][1] + p)
                dp[i + 1][j][1] = max(dp[i][j][1], dp[i][j][0] - p)
        return dp[n][-1][0]
    
# 恰好 k 次
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        f = [[[-inf] * 2 for _ in range(k + 2)] for _ in range(n + 1)]
        
        # 修改初始状态即可
        f[0][1][0] = 0
        
        for i, p in enumerate(prices):
            for j in range(1, k + 2):
                # 当前不持有股票：要么前一天就不持有，要么前一天持有今天卖出
                f[i + 1][j][0] = max(f[i][j][0], f[i][j - 1][1] + p)
                # 当前持有股票：要么前一天就持有，要么前一天不持有今天买入
                f[i + 1][j][1] = max(f[i][j][1], f[i][j][0] - p)
        
        # 返回最后一天，交易状态k+1，不持有股票的最大利润
        return f[n][k + 1][0]
    
# 至少 k 次
class Solution:
    # 递推
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        f = [[[-inf] * 2 for _ in range(k + 1)] for _ in range(n + 1)]
        f[0][0][0] = 0
        for i, p in enumerate(prices):
            # j == 0 No122
            f[i + 1][0][0] = max(f[i][0][0], f[i][0][1] + p)
            f[i + 1][0][1] = max(f[i][0][1], f[i][0][0] - p)  # 无限次
            # j != 0
            for j in range(1, k + 1):
                # f[i + 1][j][0] = max(f[i][j][0], f[i][j][1] + p)
                # f[i + 1][j][1] = max(f[i][j][1], f[i][j - 1][0] - p)
                f[i + 1][j][0] = max(f[i][j][0], f[i][j - 1][1] + p)
                f[i + 1][j][1] = max(f[i][j][1], f[i][j][0] - p)
        return f[-1][-1][0]

