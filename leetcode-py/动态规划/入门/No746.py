from functools import cache
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dfs(n):
            if n == 0 or n == 1:
                return 0
            res = min(cost[n-1]+dfs(n-1),cost[n-2]+dfs(n-2))
            return res

        return dfs(len(cost))   # 11ms
    
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        dp = [0] * (length + 1)
        for i in range(2,length+1):
            dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[length]   # 3ms
    
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        p0 = p1 =0
        for i in range(2,length+1):
            res = min(p1+cost[i-1],p0+cost[i-2])
            p0,p1 = p1,res
        return res
    
from itertools import pairwise
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f0 = f1 = 0
        for c0, c1 in pairwise(cost):
        # pairwise作用是生成序列中相邻元素的配对。
            f0, f1 = f1, min(f1 + c1, f0 + c0)
        # c0 和 c1 是 cost 中相邻的两个台阶的花费。
        return f1