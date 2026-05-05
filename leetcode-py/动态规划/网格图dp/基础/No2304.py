from math import inf
from typing import List


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[inf] * n for _ in range(m)]
        dp[0] = grid[0][:]

        for i in range(1, m):
            for j, x in enumerate(grid[i]):
                for k, c in enumerate(moveCost[x]):
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + c + x)
        
        return min(dp[m])   # 错误 用了当前格子移动的代价 应该是上个格子的移动代价



class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[inf] * n for _ in range(m)]
        dp[-1][:] = grid[-1][:]

        for i in range(m - 2, -1, -1):
            for j, x in enumerate(grid[i]):
                for k, c in enumerate(moveCost[x]):
                    dp[i][j] = min(dp[i][j], dp[i + 1][k] + c + x)
        
        return min(dp[0])
    

class Solution:
    # leetcode官方
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = grid[0]
        for i in range(1, len(grid)):
            dp = [grid[i][j] + min(dp[k] + moveCost[grid[i - 1][k]][j] for k in range(n)) for j in range(n)]
        return min(dp)

