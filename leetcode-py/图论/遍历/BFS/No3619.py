from collections import deque
from typing import List

DIR = [(0,1), (0,-1), (1,0), (-1,0)]
class Solution:
    # bfs
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        def bfs(i: int, j: int):
            res = grid[i][j]
            queue = deque([(i, j)])
            grid[i][j] = 0
            while queue:
                x, y = queue.popleft()
                for dx, dy in DIR:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny]:
                        queue.append((nx, ny))
                        res += grid[nx][ny]
                        grid[nx][ny] = 0
            return res
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    count = bfs(i, j)
                    if count % k == 0:
                        ans += 1
        
        return ans  # 267ms


