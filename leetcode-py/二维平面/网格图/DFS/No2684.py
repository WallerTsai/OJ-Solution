from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        ans = 0
        visited = set()
        def dfs(i: int, j: int):
            nonlocal ans
            ans = max(ans, j)
            if ans == n - 1:
                return 
            
            if (i, j) in visited:
                return
            
            visited.add((i, j))
            
            for k in (i - 1, i, i + 1):
                if 0 <= k < m and grid[k][j + 1] > grid[i][j]:
                    dfs(k, j + 1)
            
        for i in range(m):
            dfs(i, 0)
            if ans == n - 1:
                break

        return ans  # 39ms



class Solution:
    # 灵神
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        def dfs(i: int, j: int) -> None:
            nonlocal ans
            ans = max(ans, j)
            if ans == n - 1:  # ans 已达到最大值
                return
            for k in i - 1, i, i + 1:  # 向右上/右/右下走一步
                if 0 <= k < m and grid[k][j + 1] > grid[i][j]:
                    dfs(k, j + 1)
            grid[i][j] = 0
        for i in range(m):
            dfs(i, 0)  # 从第一列的任一单元格出发
        return ans  # 27ms


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[False] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = True

        ans = 0
        for j in range(1, n):
            for i in range(m):
                # 到达不了
                if not dp[i][j - 1]:
                    continue
                for nx in (-1, 0, 1):
                    ni = i + nx
                    if 0 <= ni < m:
                        # 已经到达过
                        if dp[ni][j]:
                            continue
                        if grid[ni][j] > grid[i][j - 1]:
                            dp[ni][j] = True
                            ans = j

            if ans == n - 1:
                return ans
            
        return ans