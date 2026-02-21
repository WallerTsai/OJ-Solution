from math import inf
from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [inf] * n

        for i in range(min(3, n)):
            dp[i] = costs[i] + pow((i - 0 + 1), 2)

        for j in range(n):
            for i in range(j + 1, min(j + 4, n)):
                dp[i] = min(dp[i], dp[j] + costs[i] + pow(i - j, 2))
        
        return dp[-1]

            

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            min_cost = inf
            for k in range(max(0, i - 3), i):
                min_cost = min(min_cost, dp[k] + costs[i - 1] + pow(i - k, 2))
            dp[i] = min_cost

        return dp[-1]


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        ans = [0] * (n + 3)
        for i in range(n):
            ans[i + 3] = costs[i] + min(ans[i + 2] + 1, ans[i + 1] + 4, ans[i] + 9)
        return ans[-1]
    
    # 这段代码非常妙
    # 索引映射关系
    # ans[3] 对应真正到达台阶 1 的最小成本
    # ......
    # ans[n+2] 对应真正到达台阶 n 的最小成本    

    
class Solution:
    def climbStairs(self, _, costs: List[int]) -> int:
        f0 = f1 = f2 = 0
        for c in costs:
            f0, f1, f2 = f1, f2, min(f0 + 9, f1 + 4, f2 + 1) + c
        return f2