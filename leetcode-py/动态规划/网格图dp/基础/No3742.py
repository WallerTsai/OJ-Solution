from functools import cache
from math import inf
from typing import List


class Solution:
    # dfs
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = -1
        def dfs(i, j, score, cost):
            cost = cost - (grid[i][j] != 0)
            if cost < 0:
                return
            score += grid[i][j]
            if i == m - 1 and j == n - 1:
                nonlocal ans
                ans = max(ans, score)
            if i < m - 1:
                dfs(i + 1, j, score, cost)
            if j < n - 1:
                dfs(i, j + 1, score, cost)

        dfs(0, 0, 0, k)
        return ans  # 超时
    
class Solution:
    # dfs
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i, j, cost):
            if i < 0 or j < 0 or cost < 0:
                return -inf
            if i == 0 and j == 0:
                return 0
            x = grid[i][j]
            if x > 0:
                cost -= 1
            return max(dfs(i - 1, j, cost), dfs(i, j - 1, cost)) + x

        ans = dfs(m - 1, n - 1, k)
        return ans if ans != -inf else -1   # 10910ms

# 手写 max 更快
max = lambda a, b: b if b > a else a

class Solution:
    # 灵神 递推
    def maxPathScore(self, grid: List[List[int]], K: int) -> int:
        m, n = len(grid), len(grid[0])
        f = [[[-inf] * (K + 2) for _ in range(n + 1)] for _ in range(m + 1)]
        f[0][1][1:] = [0] * (K + 1)  # 保证 f[1][1][k] 计算正确

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                for k in range(K + 1):
                    new_k = k - 1 if x else k
                    f[i + 1][j + 1][k + 1] = max(f[i][j + 1][new_k + 1], f[i + 1][j][new_k + 1]) + x

        ans = f[m][n][-1]
        return -1 if ans < 0 else ans



fun = Solution()
fun.maxPathScore([[0, 1],[1, 2]], 1)



max_val = lambda a, b: b if b > a else a

class Solution:
    def maxPathScore(self, grid: list[list[int]], K: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # 1. 数组第三维明确设为 K + 1
        f = [[[-inf] * (K + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        
        # 2. 初始化起点，下标 0 到 K 的状态都初始为 0
        f[0][1][:] = [0] * (K + 1)

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                for k in range(K + 1):
                    # 上一步需要的预算
                    new_k = k - 1 if x else k
                    
                    # 3. 【核心区别】显式拦截越界的非法预算
                    if new_k >= 0:
                        f[i + 1][j + 1][k] = max_val(f[i][j + 1][new_k], f[i + 1][j][new_k]) + x

        ans = f[m][n][-1] # 即 f[m][n][K]，预算为 K 时的最大得分
        return -1 if ans < 0 else ans
    


# 日期： 2026年4月30日

class Solution:
    def maxPathScore(self, grid: List[List[int]], K: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[-inf] * (K + 1) for _ in range(n + 1)] for _ in range(m + 1)]

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                cost = 1 if x > 0 else 0
                for k in range(K + 1):
                    if k < cost:
                        continue
                    if i == 0 and j == 0:
                        dp[i + 1][j + 1][k] = x
                        continue
                    dp[i + 1][j + 1][k] = max(dp[i][j + 1][k - cost], dp[i + 1][j][k - cost]) + x
        
        ans = max(dp[m][n]) # dp[m][n][k]
        return ans if ans >= 0 else -1


