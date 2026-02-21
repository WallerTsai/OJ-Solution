from functools import cache
from math import ceil


class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 5_000:
            return 1.0
        
        @cache
        def dfs(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            return (dfs(a - 100, b) + dfs(a - 75, b - 25) + dfs(a - 50, b - 50) + dfs(a - 25, b - 75)) / 4

        return dfs(n, n)    # 11ms
    
class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 5000:
            return 1.0
        
        # 每次操作都是25倍数，为了减少dp内存占用
        N = ceil(n/25)

        dp = [[0.0] * (N + 1) for _ in range(N + 1)]

        # 初始化边界
        dp[0][0] = 0.5
        for b in range(1, N + 1):
            dp[0][b] = 1.0
        
        # 从下往上
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                t1 = dp[max(a - 4, 0)][b]
                t2 = dp[max(a - 3, 0)][b-1]
                t3 = dp[max(a - 2, 0)][max(b - 2, 0)]
                t4 = dp[a - 1][max(b - 3, 0)]

                dp[a][b] = 0.25 * (t1 + t2 + t3 + t4)

        return dp[N][N] # 35ms