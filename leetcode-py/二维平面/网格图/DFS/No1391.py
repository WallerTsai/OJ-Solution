from functools import cache
from typing import List

DIRS = (
    (),                 # 占位，使得下面方向向量下标对齐
    ((0, -1), (0, 1)),  # 站在街道 1，可以往左或者往右
    ((-1, 0), (1, 0)),  # 站在街道 2，可以往上或者往下
    ((0, -1), (1, 0)),  # 站在街道 3，可以往左或者往下
    ((0, 1), (1, 0)),   # 站在街道 4，可以往右或者往下
    ((0, -1), (-1, 0)), # 站在街道 5，可以往左或者往上
    ((0, 1), (-1, 0)),  # 站在街道 6，可以往右或者往上
)

DIR = {
    1: [(0, -1), (0, 1)],
    2: [(-1, 0), (1, 0)],
    3: [(0, -1), (1, 0)],
    4: [(0, 1), (1, 0)],
    5: [(0, -1), (-1, 0)],
    6: [(0, 1), (-1, 0)]
    }


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = set()

        @cache
        def dfs(x: int, y: int):
            if x == m - 1 and y == n - 1:
                return True
            
            visited.add((x, y))
            for dx, dy in DIR[grid[x][y]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and (-dx, -dy) in DIR[grid[nx][ny]]:
                    if dfs(nx, ny):
                        return True
                    
            return False
        
        ans = dfs(0, 0)
        dfs.cache_clear()
        return ans