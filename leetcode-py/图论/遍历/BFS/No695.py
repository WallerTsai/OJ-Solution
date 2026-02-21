from collections import deque
from typing import List

di = [(0,1), (0,-1), (1,0), (-1,0)]
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        def bfs(i: int, j: int) -> int:
            count = 1
            grid[i][j] = 0
            queue = deque([(i,j)])

            while queue:
                x, y = queue.popleft()
                for dx, dy in di:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny]:
                        queue.append((nx,ny))
                        count += 1
                        grid[nx][ny] = 0
            
            return count
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    ans = max(ans,bfs(i,j))

        return ans