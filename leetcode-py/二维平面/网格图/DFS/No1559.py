from typing import List


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        DIR = (1, 0), (0, 1), (-1, 0), (0, -1)
        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j, pre):
            visited.add((i, j))
            for dx, dy in DIR:
                nx, ny = i + dx, j + dy
                if (nx, ny) != pre and 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == grid[i][j]:
                    if (nx, ny) in visited:
                        return True
                    if dfs(nx, ny, (i, j)):
                        return True
            return False
        
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and dfs(i, j, (-1, -1)):
                    return True
        return False


