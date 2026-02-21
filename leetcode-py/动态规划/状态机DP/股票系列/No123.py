from itertools import pairwise
from math import inf
from typing import List


    
class Solution:
    # No.188
    # 递推 + 空间优化
    def No188maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[-inf] * 2 for _ in range(k + 2)]
        for j in range(1, k + 2):
            dp[j][0] = 0
        for i, p in enumerate(prices):
            for j in range(1, k + 2):
                dp[j][0] = max(dp[j][0], dp[j - 1][1] + p)
                dp[j][1] = max(dp[j][1], dp[j][0] - p)
        return dp[-1][0]
    
    def maxProfit(self, prices: List[int]) -> int:
        return self.No188maxProfit(2,prices)    # 612ms
    

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans1 = ans2 = 0
        pre_min = inf
        profit = 0
        # t = 0   # 计数
        prices.append(-1) # 哨兵
        for p in prices:
            if p < pre_min:
                pre_min = p
                # t += 1
                if profit >= ans1:
                    ans2 = ans1
                    ans1 = profit
                elif profit > ans2:
                    ans2 =profit
                profit = 0
            else:
                profit = max(profit, p - pre_min)
        
        return ans1 + ans2  # 错误
    
# 每次在局部最高点提现
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans1 = ans2 = 0
        profit = 0
        prices.append(-1) # 哨兵
        for p1, p2 in pairwise(prices):
            if p2 < p1 :
                if profit >= ans1:
                    ans2 = ans1
                    ans1 = profit
                elif profit > ans2:
                    ans2 =profit
                profit = 0
            else:
                profit += p2 - p1
        
        return ans1 + ans2  # 错误
    

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 第一次买入，第一次卖出，第二次买入，第二次卖出
        f1, f2, f3, f4 = -prices[0], 0, -prices[0], 0
        for price in prices[1:]:
            f1 = max(f1, -price)
            f2 = max(f2, f1 + price)
            f3 = max(f3, f2 - price)
            f4 = max(f4, f3 + price)
        return f4   # 251ms