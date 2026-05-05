from functools import cache
from math import inf
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        @cache
        def dfs(i: int, j: int):
            if j < 0 or j >= n:
                return inf
            if i == 0:
                return matrix[0][j]
            return min(dfs(i - 1, j - 1), dfs(i - 1, j), dfs(i - 1, j + 1)) + matrix[i][j]
        
        return min(dfs(n - 1, j) for j in range(n))


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[inf] * (n + 2) for _ in range(n)]
        for i in range(1, n + 1):
            dp[0][i] = matrix[0][i - 1]

        for i in range(1, n):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j - 1]
    
        return min(dp[n - 1])



class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        f = [inf] + matrix[0] + [inf]
        for row in matrix[1:]:
            pre = f[0]  # 充当 f[c]
            for c, x in enumerate(row):
                pre, f[c + 1] = f[c + 1], min(pre, f[c + 1], f[c + 2]) + x
        return min(f)

