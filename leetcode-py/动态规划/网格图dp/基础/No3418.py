from functools import cache
from math import inf
from typing import List


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])

        @cache
        def dfs(i: int, j: int, t: int) -> int:
            if i < 0 or j < 0 or t < 0:
                return -inf
            
            x = coins[i][j]
            if i == 0 and j == 0:
                if x < 0 and t:
                    return 0
                return x
            
            res = max(dfs(i - 1, j, t), dfs(i, j - 1, t)) + x
            if x < 0 and t:
                res = max(res, dfs(i - 1, j, t - 1), dfs(i, j - 1, t - 1))
            return res
        
        ans = dfs(m - 1, n - 1, 2)
        return ans  # 5633ms
    

class Solution:
    # 递推
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        dp = [[[-inf] * 3 for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][1] = [0] * 3

        for i, row in enumerate(coins):
            for j, x in enumerate(row):
                dp[i + 1][j + 1][0] = max(dp[i + 1][j][0],dp[i][j + 1][0]) + x

                dp[i + 1][j + 1][1] = max(dp[i + 1][j][1] + x, dp[i][j + 1][1] + x,
                                          dp[i + 1][j][0], dp[i][j + 1][0])
                
                dp[i + 1][j + 1][2] = max(dp[i + 1][j][2] + x, dp[i][j + 1][2] + x,
                                          dp[i + 1][j][1], dp[i][j + 1][1])
        
        return dp[m][n][2]  # 2147ms
    

class Solution:
    # 递推 + 空间优化
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        dp = [[-inf] * 3 for _ in range(n + 1)]
        dp[1] = [0] * 3

        for row in coins:
            for j, x in enumerate(row):
                dp[j + 1][2] = max(dp[j][2] + x, dp[j + 1][2] + x, dp[j][1], dp[j + 1][1])
                
                dp[j + 1][1] = max(dp[j][1] + x, dp[j + 1][1] + x, dp[j][0], dp[j + 1][0])
                
                dp[j + 1][0] = max(dp[j][0],dp[j + 1][0]) + x

        return dp[n][2] # 1330ms