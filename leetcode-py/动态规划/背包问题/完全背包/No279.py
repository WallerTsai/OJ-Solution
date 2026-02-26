from functools import cache
from math import inf, isqrt


class Solution:
    def numSquares(self, n: int) -> int:
        @cache
        def dfs(i: int, j: int):
            if i == 0:
                return inf if j else 0
            if j < i ** 2:
                return dfs(i - 1, j)
            return min(dfs(i - 1, j), dfs(i, j - i ** 2) + 1)
        ans = dfs(isqrt(n), n)
        dfs.cache_clear()
        return ans
        


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [inf] * n
        for i in range(1, isqrt(n) + 1):
            for j in range(i ** 2, n + 1):
                dp[j] = min(dp[j], dp[j - i ** 2] + 1)
        return dp[n]


