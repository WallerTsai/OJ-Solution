from functools import cache
from math import inf


class Solution:
    def minCost(self, n: int) -> int:
        @cache
        def dfs(i: int):
            if i < 2:
                return 0
            res = inf
            for j in range(1, i + 1):
                res = min(res, dfs(i - j) + dfs(j) + j * (i - j))
            return res
        ans = dfs(n)
        dfs.cache_clear()
        return ans
    
Solution().minCost(3)