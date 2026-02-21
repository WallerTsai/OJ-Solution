from functools import cache


class Solution:
    # 抄写灵神
    def palindromePartition(self, s: str, k: int) -> int:
        @cache
        def min_change(l: int,r: int) -> int:
            if l >= r:
                return 0
            return s[l] != s[r] + min_change(l + 1, r + 1)
        
        @cache
        def dfs(i:int, r:int) -> int:
            if i == 0:
                return min_change(0,r)
            return min(dfs(i-1,l-1) + min_change(l,r) for l in range(i, r+1))

        return dfs(k-1,len(s)-1)

class Solution:
    # 抄写灵神
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        min_change = [[0] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i+1,n):
                min_change[i][j] = min_change[i+1][j-1] + (s[i] != s[j])

        dp = [[0] * n for _ in range(k)]
        dp[0] = min_change[0]
        for i in range(1,k):
            for r in range(i, n - (k - 1 - i)):
                dp[i][r] = min(dp[i-1][l-1] + min_change[l][r] for l in range(i,r+1))
        
        return dp[k-1][n-1]