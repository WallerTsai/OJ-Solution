from functools import cache


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def pow_cache(i: int) -> int:
            return pow(i, x)
        
        @cache
        def dfs(i: int, target: int):
            if target == 0:
                return 1
            res = 0
            while pow_cache(i) <= target:
                res += dfs(i + 1, target - pow_cache(i))
                i += 1
            return res
        
        pow_cache.cache_clear()
        dfs.cache_clear()
        return dfs(1, n) % MOD  # 超时

# 这道题应该是 0-1 背包问题 考虑选和不选
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def pow_cache(i: int) -> int:
            return pow(i, x)
        
        @cache
        def dfs(i: int, target: int):
            if target == 0:
                return 1
            if pow_cache(i) > target:
                return 0
            
            res = dfs(i + 1, target - pow_cache(i)) + dfs(i + 1, target)

            return res % MOD
        
        pow_cache.cache_clear()
        dfs.cache_clear()
        return dfs(1, n) % MOD  # 2567ms
    

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def pow_cache(i: int) -> int:
            return pow(i, x)

        MX = int(pow(n + 1, 1 / x)) # 注意这里会精度丢失 所以要传 n + 1 例：64 3

        dp = [[0] * (n + 1) for _ in range(MX + 1)]
        dp[0][0] = 1

        for i in range(1, MX + 1):
            for t in range(n + 1):
                dp[i][t] = dp[i - 1][t] # 不选
                if t >= pow_cache(i):
                    dp[i][t] += dp[i - 1][t - pow_cache(i)]
                dp[i][t] %= MOD
        pow_cache.cache_clear()
        return dp[-1][-1]   # 1738ms
    
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7
        
        dp = [1] + [0] * n

        for i in range(1, n + 1):
            powx = pow(i, x)
            if i > n:
                break
            for t in range(n, powx - 1, -1):
                dp[t] += dp[t - powx]

        return dp[n] % MOD  # 247ms