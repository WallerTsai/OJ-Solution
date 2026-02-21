from functools import cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def dfs(l: int, r: int) -> int:
            if l > r:
                return 0
            if l == r:
                return 1
            if s[l] == s[r]:
                return dfs(l + 1, r - 1) + 2
            # 不等的情况
            return max(dfs(l + 1, r),dfs(l, r - 1))

        return dfs(0,len(s) - 1)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for l in range(n - 1, -1, -1):
            dp[l][l] = 1
            for r in range(l + 1,n):
                if s[l] == s[r]:
                    dp[l][r] = dp[l+1][r-1] + 2
                else:
                    dp[l][r] = max(dp[l+1][r],dp[l][r-1])
        return dp[0][n-1]
    
class Solution:
    # 灵神
    # 空间优化：难理解
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        f = [0] * n
        for i in range(n - 1, -1, -1):
            f[i] = 1
            pre = 0  # 初始值为 f[i+1][i]
            for j in range(i + 1, n):
                tmp = f[j]
                f[j] = pre + 2 if s[i] == s[j] else max(f[j], f[j - 1])
                pre = tmp
        return f[-1]