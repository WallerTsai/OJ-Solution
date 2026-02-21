from functools import cache


class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        @cache
        def dfs(i):
            if i == 1:
                return 1
            res = i
            for x in range(1, (i + 1) // 2 + 1):
                res = max(res, x * dfs(i - x))
            return res
        
        return dfs(n)   # 3ms
    
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 0, 0, 1
        for i in range(3, n + 1):
            for j in range(1, i // 2 + 1):
                dp[i] = max(j * dp[i - j], j * (i - j), dp[i])
        return dp[-1]   # 2ms


class Solution:
    # 数学
    # https://leetcode.cn/problems/integer-break/solutions/29098/343-zheng-shu-chai-fen-tan-xin-by-jyd/
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        d, m = divmod(n, 3)
        
        if m == 0:
            return pow(3, d)
        if m == 1:
            return pow(3, d - 1) * (3 + 1)
        if m == 2:
            return pow(3, d) * 2    # 0ms