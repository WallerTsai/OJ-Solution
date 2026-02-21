from functools import cache
from typing import List


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        DIRS = (1, 1), (1, -1), (-1, -1), (-1, 1)
        n, m = len(grid), len(grid[0])

        # 这里的i, j 为上一步的坐标
        @cache
        def dfs(i: int, j: int, k: int, can_turn: bool, target: int) -> int:
            i += DIRS[k][0]
            j += DIRS[k][1]

            if not(0 <= i < n and 0 <= j < m) or grid[i][j] != target:
                return 0
            
            res = dfs(i, j, k, can_turn, 2 - target)    # 2 - target 实现 2,0,2,0 跳转
            if can_turn:
                res = max(res, dfs(i, j, (k + 1) % 4, False, 2 - target))
            
            return res + 1


        ans = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    for k in range(4):
                        ans = max(ans, dfs(i, j, k, True, 2) + 1) # 注意这里的+1

        return ans
    
class Solution:
    # cv from 灵神
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        DIRS = (1, 1), (1, -1), (-1, -1), (-1, 1)
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i: int, j: int, k: int, can_turn: bool, target: int) -> int:
            i += DIRS[k][0]
            j += DIRS[k][1]
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != target:
                return 0
            res = dfs(i, j, k, can_turn, 2 - target)
            if can_turn:
                maxs = (m - i - 1, j, i, n - j - 1)  # 理论最大值（走到底）
                k = (k + 1) % 4
                # 优化二：如果理论最大值没有超过 res，那么不递归
                if maxs[k] > res:
                    res = max(res, dfs(i, j, k, False, 2 - target))
            return res + 1

        ans = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x != 1:
                    continue
                maxs = (m - i, j + 1, i + 1, n - j)  # 理论最大值（走到底）
                for k, mx in enumerate(maxs):  # 枚举起始方向
                    # 优化一：如果理论最大值没有超过 ans，那么不递归
                    if mx > ans:
                        ans = max(ans, dfs(i, j, k, True, 2) + 1)
        return ans