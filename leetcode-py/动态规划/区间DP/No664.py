# 难点在于状态的定义

# 状态定义:
# f[i][j] 表示打印区间 s[i...j] 的最少次数

# 状态转移 (Case Analysis):
# 1. 当 s[i] == s[j] 时:
#    f[i][j] = f[i][j - 1]
#    (解释: 打印 s[j] 可以顺便在打印 s[i] 的那一笔中完成，不需要额外次数)

# 2. 当 s[i] != s[j] 时:
#    f[i][j] = min_{i <= k < j} { f[i][k] + f[k + 1][j] }
#    (解释: 将区间在 k 处拆分为两部分，取所有拆分方案的最小值)

from functools import cache
from math import inf


class Solution:
    def strangePrinter(self, s: str) -> int:
        # 预处理
        li = [s[0]]
        n = len(s)
        for i in range(1, n):
            if s[i] != s[i - 1]:
                li.append(s[i])

        @cache
        def dfs(left, right):
            if left == right:
                return 1
            if li[left] == li[right]:
                return dfs(left, right - 1)
            
            res = inf
            for k in range(left, right):
                res = min(res, dfs(left, k) + dfs(k + 1, right))

            return res
        
        ans = dfs(0, len(li) - 1)
        dfs.cache_clear()
        return ans
    

class Solution:
    def strangePrinter(self, s: str) -> int:
        # 预处理
        li = [s[0]]
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                li.append(s[i])

        n = len(li)
        dp = [[1] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if li[i] == li[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    tmp = inf
                    for k in range(i, j):
                        tmp = min(tmp, dp[i][k] + dp[k + 1][j])
                    dp[i][j] = tmp
        
        return dp[0][n - 1]