from functools import cache
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        @cache
        def dfs(i: int, j: int):
            if i == n - 1:
                return triangle[i][j]
            return triangle[i][j] + min(dfs(i + 1, j), dfs(i + 1, j + 1))
        
        return dfs(0, 0)    # 25ms
    


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        dp = [[0] * (i + 1) for i in range(n)]
        dp[-1] = triangle[-1]
        for i in range(n - 2, -1, -1):
            for j, x in enumerate(triangle[i]):
                dp[i][j] = x + min(dp[i + 1][j], dp[i + 1][j + 1])

        return dp[0][0] # 5ms
    
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = triangle[-1][:]
        for i in range(n - 2, -1, -1):
            for j, x in enumerate(triangle[i]):
                f[j] = min(f[j], f[j + 1]) + x
        return f[0]
    
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0][0]   # 3ms


