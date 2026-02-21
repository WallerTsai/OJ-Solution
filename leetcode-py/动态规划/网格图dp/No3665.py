from functools import cache
from typing import List

# 这道题类似于 No62

MOD = 1_000_000_007
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        DIR = (0, 1), (1, 0)

        @cache
        def dfs(i: int, j: int) -> int:
            if i == m or j == n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            
            res = 0

            for x, y in DIR:
                ni, nj = i + x, j + y
                while ni < m and nj < n and grid[ni][nj]:   # 下一步是镜子，则一直穿越
                    ni += y
                    nj += x
                    x, y = y, x
                res += dfs(ni, nj)
            
            return res % MOD
        
        return dfs(0,0) % MOD   # 1772ms
    
MOD = 1_000_000_007
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # dp[i][j][0]：从左边进入 (i,j) 的路径数
        # dp[i][j][1]：从上面进入 (i,j) 的路径数
        dp = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0][0] = dp[0][0][1] = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dp[i][j + 1][0] += dp[i][j][1]
                    dp[i + 1][j][1] += dp[i][j][0]
                else:
                    dp[i][j + 1][0] += dp[i][j][0] + dp[i][j][1]
                    dp[i + 1][j][1] += dp[i][j][0] + dp[i][j][1]

        return (sum(dp[m - 1][n - 1]) // 2)% MOD    # 2117ms


MOD = 1_000_000_007
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # dp[i][j][0]：从左边进入 (i,j) 的路径数
        # dp[i][j][1]：从上面进入 (i,j) 的路径数
        dp = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0][0]= 1  # 假设从右边进来
        dp[0][0][1] = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dp[i][j + 1][0] += dp[i][j][1]
                    dp[i + 1][j][1] += dp[i][j][0]
                else:
                    dp[i][j + 1][0] += dp[i][j][0] + dp[i][j][1]
                    dp[i + 1][j][1] += dp[i][j][0] + dp[i][j][1]

        return sum(dp[m - 1][n - 1])% MOD   # 2134ms
    
MOD = 1_000_000_007
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # dp[i][j][0]：从左边进入 (i,j) 的路径数
        # dp[i][j][1]：从上面进入 (i,j) 的路径数
        dp = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][1][0]= 1 
        dp[1][0][1] = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dp[i][j + 1][0] += dp[i][j][1]
                    dp[i + 1][j][1] += dp[i][j][0]
                else:
                    dp[i][j + 1][0] += dp[i][j][0] + dp[i][j][1]
                    dp[i + 1][j][1] += dp[i][j][0] + dp[i][j][1]

        return sum(dp[m - 1][n - 1])% MOD   # 2064ms
    

class Solution:
    # 灵神
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 1_000_000_007
        m, n = len(grid), len(grid[0])
        f = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
        # 实际 k 是i,j点走下一步的方向
        f[0][1] = [1, 1]  # 原理见 62 题我的题解
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 0:
                    f[i + 1][j + 1][0] = (f[i + 1][j][0] + f[i][j + 1][1]) % MOD
                    f[i + 1][j + 1][1] = f[i + 1][j + 1][0]
                else:
                    f[i + 1][j + 1][0] = f[i][j + 1][1]
                    f[i + 1][j + 1][1] = f[i + 1][j][0]
        return f[m][n][0]
