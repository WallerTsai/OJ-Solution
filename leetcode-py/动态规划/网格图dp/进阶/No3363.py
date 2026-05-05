from functools import cache
from typing import List


class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        # 左上角朋友只有一条路径能走
        ans = sum(row[i] for i, row in enumerate(fruits))

        n = len(fruits)

        @cache
        def dfs(i: int, j: int) -> int:
            if not (n - 1 - i) <= j < n:
                return -1
            if i == 0:
                return fruits[i][j]
            return max(dfs(i - 1, j - 1), dfs(i - 1, j), dfs(i - 1, j + 1)) + fruits[i][j]

        ans += dfs(n - 2, n - 1) # 从下往上走
        dfs.cache_clear()

        # 反转矩阵
        fruits = list(zip(*fruits))
        ans += dfs(n - 2, n - 1)
        dfs.cache_clear()
        
        return ans  # 1343ms
    
class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        def dp(fruits: List[List[int]]) -> int:
            n = len(fruits)
            f = [[-1] * (n + 1) for _ in range(n - 1)]
            f[0][n - 1] = fruits[0][-1]
            for i in range(1, n - 1):
                for j in range(max(n - 1 - i, i + 1), n):
                    f[i][j] = max(f[i - 1][j - 1], f[i - 1][j], f[i - 1][j + 1]) + fruits[i][j]
            return f[-1][n - 1]

        ans = sum(row[i] for i, row in enumerate(fruits))
        return ans + dp(fruits) + dp(list(zip(*fruits)))    # 468ms
