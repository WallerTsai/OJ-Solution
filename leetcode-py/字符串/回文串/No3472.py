from functools import cache


class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        s = list(map(ord,s))
        n = len(s)

        @cache
        def dfs(l: int, r: int, k: int) -> int:
            if l > r:
                return 0
            if l == r:
                return 1
            
            # 其中一个不选
            res = max(dfs(l+1,r,k),dfs(l,r-1,k))
            # 两个都选
            d = abs(s[l] - s[r])
            need = min(d,26 - d)
            if need <= k:
                res = max(res,dfs(l + 1, r - 1, k - need) + 2)
            
            return res

        ans = dfs(0,n-1,k)
        return ans  # 爆内存

class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        s = list(map(ord,s))
        n = len(s)

        @cache
        def dfs(l: int, r: int, k: int) -> int:
            if l > r:
                return 0
            if l == r:
                return 1
            
            # 其中一个不选
            res = max(dfs(l+1,r,k),dfs(l,r-1,k))
            # 两个都选
            d = abs(s[l] - s[r])
            need = min(d,26 - d)
            if need <= k:
                res = max(res,dfs(l + 1, r - 1, k - need) + 2)
            
            return res

        ans = dfs(0,n-1,k)
        dfs.cache_clear() #解决爆内存
        return ans  # 6814ms
    
class Solution:
    # 递推
    # 灵神
    def longestPalindromicSubsequence(self, s: str, K: int) -> int:
        s = list(map(ord, s))  # 避免频繁计算 ord
        n = len(s)
        cnt = 0
        for i in range(n // 2):
            d = abs(s[i] - s[-1 - i])
            cnt += min(d, 26 - d)
        if cnt <= K:
            return n

        f = [[[0] * n for _ in range(n)] for _ in range(K + 1)]
        for k in range(K + 1):
            for i in range(n - 1, -1, -1):
                f[k][i][i] = 1
                for j in range(i + 1, n):
                    res = max(f[k][i + 1][j], f[k][i][j - 1])
                    d = abs(s[i] - s[j])
                    op = min(d, 26 - d)
                    if op <= k:
                        res = max(res, f[k - op][i + 1][j - 1] + 2)
                    f[k][i][j] = res
        return f[K][0][-1]