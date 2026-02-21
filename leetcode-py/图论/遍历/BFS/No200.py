from typing import List
from collections import deque

di = [(0,1), (0,-1), (1,0), (-1,0)]
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        def bfs(i: int, j: int) -> None:
            queue = deque([(i,j)])
            grid[i][j] = "0"
            while queue:
                x, y = queue.popleft()
                for dx,dy in di:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "1":
                        queue.append([nx,ny])
                        grid[nx][ny] = "0"

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    bfs(i,j)
                    ans += 1
        
        return ans