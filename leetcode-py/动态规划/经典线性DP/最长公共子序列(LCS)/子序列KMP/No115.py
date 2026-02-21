from functools import cache

# https://leetcode.cn/problems/distinct-subsequences/solutions/3060706/jiao-ni-yi-bu-bu-si-kao-dpcong-ji-yi-hua-9va6/
class Solution:
    # 递归
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if j < 0: return 1
            if i < j: return 0
            res = dfs(i - 1, j) # 不选
            if s[i] == t[j]:
                res += dfs(i - 1, j - 1)
            return res
        return dfs(len(s) - 1, len(t) - 1)
    
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if n < m: return 0

        dp = [[1] + [0] * m for _ in range(n + 1)]
        for i, x in enumerate(s):
            for j, y in enumerate(t):
                dp[i + 1][j + 1] = dp[i][j + 1]
                if x == y:
                    dp[i + 1][j + 1] += dp[i][j]

        return dp[n][m]

class Solution:
    # 递推
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if n < m: return 0

        dp = [[1] + [0] * m for _ in range(n + 1)]
        for i, x in enumerate(s):
            for j in range(max(m - (n - i), 0),min(i + 1, m)):
                dp[i + 1][j + 1] = dp[i][j + 1]
                if x == t[j]:
                    dp[i + 1][j + 1] += dp[i][j]

        return dp[n][m]
    
class Solution:
    # 空间优化
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if n < m:
            return 0

        f = [1] + [0] * m
        for i, x in enumerate(s):
            for j in range(min(i, m - 1), max(m - n + i, 0) - 1, -1):
                if x == t[j]:
                    f[j + 1] += f[j]
        return f[m]
    

# 2026年1月10日
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if n < m:
            return 0
        
        dp = [[1] + [0] * m for _ in range(n + 1)]

        for i, x in enumerate(s):
            for j, y in enumerate(t):
                dp[i + 1][j + 1] = dp[i][j + 1]
                if x == y:
                    dp[i + 1][j + 1] += dp[i][j]
        
        return dp[n][m]


