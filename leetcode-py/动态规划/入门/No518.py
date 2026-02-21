from functools import cache
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        length = len(coins)
        coins.sort()
        @cache
        def dfs(i,n):
            if n == 0:
                return 1
            res = 0
            for x in range(i,length):
                if coins[x] > n:
                    break
                res += dfs(x,n-coins[x])
            return res
        return dfs(0,amount)  # 超时
    
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        length = len(coins)
        @cache
        def dfs(i,n):
            if i >= length:
                return 1 if n == 0 else 0
            if n < coins[i]:
                return dfs(i+1,n)
            return dfs(i+1,n) + dfs(i,n-coins[i]) 
        return dfs(0,amount)    # 862ms
    
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, c: int) -> int:
            if i < 0:
                return 1 if c == 0 else 0
            if c < coins[i]:
                return dfs(i - 1, c)
            return dfs(i - 1, c) + dfs(i, c - coins[i])
        return dfs(len(coins) - 1, amount) # 359ms
    #  这个缓存命中率高

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        length = len(coins)
        dp = [[0] * (amount +  1) for _ in range(length+1)]
        dp[0][0] = 1

        for i,c in enumerate(coins):
            for x in range(amount+1):
                if x < c:
                    dp[i+1][x] = dp[i][x]
                else:
                    dp[i+1][x] = dp[i][x] + dp[i+1][x-c]
        return dp[length][amount]   # 259ms
    
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount +  1)
        dp[0] = 1
        for c in coins:
            for x in range(c,amount+1):
                dp[x] += dp[x-c]
        return dp[amount]