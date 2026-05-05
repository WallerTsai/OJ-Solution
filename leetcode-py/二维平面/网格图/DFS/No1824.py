from collections import deque
from functools import cache
from math import inf
from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        m, n = 3, len(obstacles)

        @cache
        def dfs(i: int, j: int):
            if j == n - 1:
                return 0
            
            # 贪心
            if obstacles[j + 1] != i:
                return dfs(i, j + 1)
            
            res = inf
            for nx in (1, 2, 3):
                if nx != i and obstacles[j] != nx:
                    res = min(res, dfs(nx, j + 1) + 1)
            
            return res
        
        ans = dfs(2, 0)
        dfs.cache_clear()

        return ans  # 超时
    

class Solution:
    # 填表法
    def minSideJumps(self, obstacles: List[int]) -> int:
        m, n = 3, len(obstacles)
        dp = [[inf] * 3 for _ in range(n)]
        dp[0][0] = 1
        dp[0][1] = 0
        dp[0][2] = 1

        for i in range(1, n):
            # 不跳
            for j in range(3):
                if obstacles[i] != j + 1:
                    dp[i][j] = dp[i - 1][j]
            # 跳
            for j in range(3):
                if obstacles[i] == j + 1:
                    continue
                for pre in range(3):
                    if pre != j:
                        dp[i][j] = min(dp[i][j], dp[i][pre] + 1)
        
        return min(dp[n - 1])   # 2000ms


class Solution:
    def minSideJumps(self, obstacles: list[int]) -> int:

        dp = [1, 0, 1]
        for obs in obstacles[1:]:
            if obs > 0:
                dp[obs - 1] = inf
                
            # 处理侧跳 获取当前三条车道直行过来的最小代价
            min_val = min(dp)
            
            for j in range(3):
                if j != obs - 1:
                    dp[j] = min(dp[j], min_val + 1)
                    
        return min(dp)  # 623ms


class Solution:
    # 灵神
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dis = [[n] * 3 for _ in range(n)]
        dis[0][1] = 0
        q = deque([(0, 1)])  # 起点
        while True:
            i, j = q.popleft()
            d = dis[i][j]
            if i == n - 1: return d  # 到达终点
            if obstacles[i + 1] != j + 1 and d < dis[i + 1][j]:  # 向右
                dis[i + 1][j] = d
                q.appendleft((i + 1, j))  # 加到队首
            for k in (j + 1) % 3, (j + 2) % 3:  # 枚举另外两条跑道（向上/向下）
                if obstacles[i] != k + 1 and d + 1 < dis[i][k]:
                    dis[i][k] = d + 1
                    q.append((i, k))  # 加到队尾

