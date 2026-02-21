from math import inf
from typing import List


class Solution:
    # 后缀最大值
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        suf_max = prices[-1]
        ans = 0
        for i in range(n - 2, -1, -1):
            if prices[i] < suf_max:
                ans = max(ans, suf_max - prices[i])
            else:
                suf_max = prices[i]
        return ans
    
class Solution:
    # 前缀最小值
    def maxProfit(self, prices: List[int]) -> int:
        cost, profit = inf, 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit