from functools import cache
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        length,width = len(obstacleGrid[0]),len(obstacleGrid)
        @cache
        def dfs(x:int,y:int):
            if not (0 <= x < length) or not (0 <= y < width):
                return 0
            if obstacleGrid[y][x]:
                return 0
            if x == length-1  and y == width-1:
                return 1
            path = 0
            # 向右:
            path += dfs(x+1,y)
            # 向下：
            path += dfs(x,y+1)

            return path
        
        return dfs(0,0)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（一行代码实现记忆化）
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0 or obstacleGrid[i][j]:
                return 0
            if i == 0 and j == 0:
                return 1
            return dfs(i - 1, j) + dfs(i, j - 1)

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        return dfs(m - 1, n - 1)
    
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n + 1) for _ in range(m+1)]
        dp[1][1] = 1
        for i,row in enumerate(obstacleGrid):
            for j,x in enumerate(row):
                if x == 0:
                    dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1]
        return dp[m][n]     # 这里修改了dp[1][1]

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n + 1) for _ in range(m+1)]
        dp[1][1] = 1
        for i,row in enumerate(obstacleGrid):
            for j,x in enumerate(row):
                if x == 0:
                    dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1]
        return dp[m][n]

# 空间优化
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n =len(obstacleGrid[0])
        dp = [0] * (n + 1)
        dp[1] = 1
        for row in obstacleGrid:
            for j,x in enumerate(row):
                if x == 0:
                    dp[j+1] += dp[j]
                else:
                    dp[j+1] = 0
        return dp[n]
# 举个例子，在计算 f[1][1] 时，会用到 f[0][1]，但是之后就不再用到了。
# 那么干脆把 f[1][1] 记到 f[0][1] 中，这样对于 f[1][2] 来说，
# 它需要的数据就在 f[0][1] 和 f[0][2] 中。f[1][2] 算完后也可以同样记到 f[0][2] 中。
