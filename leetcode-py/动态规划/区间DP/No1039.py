from functools import cache
from typing import List

# 以下均是灵神代码

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        @cache
        def dfs(i: int, j: int) -> int:
            if i + 1 == j:
                return 0
            return min(dfs(i, k) + dfs(k, j) + values[i] * values[j] * values[k] for k in range(i + 1, j))

        return dfs(0, len(values) - 1)


class Solution:
    def minScoreTriangulation(self, v: List[int]) -> int:
        n = len(v)
        f = [[0] * n for _ in range(n)]
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                f[i][j] = min(f[i][k] + f[k][j] + v[i] * v[j] * v[k]
                              for k in range(i + 1, j))
        return f[0][-1]