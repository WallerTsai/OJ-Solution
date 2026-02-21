from functools import cache


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        @cache
        def dfs(i: int) -> int:
            if k <= i <= n:
                return 1.0
            if i >= n:
                return 0.0
            s = 0
            for j in range(1, maxPts + 1):
                s += dfs(i + j)

            return s / maxPts
        dfs.cache_clear()
        return dfs(0)   # 超时
    
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp=[None]*(K+W)
        s=0
        for i in range(K,K+W):          # 填蓝色的格子
            dp[i] = 1 if i<=N else 0
            s+=dp[i]
        for i in range(K-1,-1,-1):      # 填橘黄色格子
            dp[i]=s/W
            s=s-dp[i+W]+dp[i]
        return dp[0]