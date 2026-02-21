from functools import cache
from typing import List


DIR = (1, 0), (0, 1)

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 1_000_000_007
        m, n = len(grid), len(grid[0])
        @cache
        def dfs(i, j, t):
            if i < 0 or j < 0:
                return 0
            if i == j == 0:
                return 1 if t == 0 else 0
            nx_t = (t + grid[i][j]) % k
            return (dfs(i - 1, j, nx_t) + dfs(i, j - 1, nx_t)) % MOD
        
        return dfs(m - 1, n - 1, 0) # 错误，小细节没处理好


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 1_000_000_007
        m, n = len(grid), len(grid[0])
        @cache
        def dfs(i, j, t):
            if i < 0 or j < 0:
                return 0
            
            nx_t = (t + grid[i][j]) % k

            if i == j == 0:
                return 1 if nx_t == 0 else 0
            
            return (dfs(i - 1, j, nx_t) + dfs(i, j - 1, nx_t)) % MOD
        
        dfs.cache_clear()
        return dfs(m - 1, n - 1, 0) # 爆内存，小细节


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 1_000_000_007
        m, n = len(grid), len(grid[0])
        @cache
        def dfs(i, j, t):
            if i < 0 or j < 0:
                return 0
            
            nx_t = (t + grid[i][j]) % k

            if i == j == 0:
                return 1 if nx_t == 0 else 0
            
            return (dfs(i - 1, j, nx_t) + dfs(i, j - 1, nx_t)) % MOD
        
        ans = dfs(m - 1, n - 1, 0)
        dfs.cache_clear()
        return ans  # 3780ms
    
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 1_000_000_007
        m, n = len(grid), len(grid[0])
        
        dp = [[[0] * k for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][1][0] = 1 # 一个方向进入(0, 0) 就行了
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                for t in range(k):
                    pre_t = (t - x) % k
                    dp[i + 1][j + 1][t] = (dp[i + 1][j][pre_t] + dp[i][j + 1][pre_t]) % MOD
        
        return dp[m][n][0]  # 1607ms
        

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 1_000_000_007
        m, n = len(grid), len(grid[0])
        f = [[0] * k for _ in range(n + 1)]
        f[1][0] = 1
        for row in grid:
            for j, x in enumerate(row):
                new_f = [0] * k  # 为避免提前把 f[j+1][s] 覆盖，先保存到 new_f[s] 中
                for s in range(k):
                    new_s = (s + x) % k
                    new_f[s] = (f[j + 1][new_s] + f[j][new_s]) % MOD
                f[j + 1] = new_f  # 循环结束后再赋给 f[j+1]
        return f[n][0]  # 827ms

