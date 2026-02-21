from functools import cache


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def dfs(i: int):
            if i >= n:
                return 1
            res = 0
            if n - i >= 3:
                res += 2 * dfs(i + 3) % MOD
            if n - i >= 2:
                res += dfs(i + 2) % MOD
            res += dfs(i + 1) % MOD

            return res % MOD
        
        return dfs(0)   # n = 4 错误，有奇怪东西
    
    
MOD = 1_000_000_007

class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        f = [0] * (n + 1)
        f[0] = f[1] = 1
        f[2] = 2
        for i in range(3, n + 1):
            f[i] = (f[i - 1] * 2 + f[i - 3]) % MOD
        return f[n]
