from functools import cache


class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        n = zero + one
        MOD = 1_000_000_007

        @cache
        def dfs(i: int, zero_num: int, one_num: int, last_zero_idx: int, last_one_idx: int):
            if i == n:
                return 1 
            res = 0

            if zero_num > 0 and i - last_zero_idx > limit:
                res = (res + dfs(i + 1, zero_num - 1, one_num, i, last_one_idx)) % MOD
                return res
            
            if one_num > 0 and i - last_one_idx > limit:
                res = (res + dfs(i + 1, zero_num, one_num - 1, last_zero_idx, i)) % MOD
                return res
            
            if zero_num > 0:
                res = (res + dfs(i + 1, zero_num - 1, one_num, i, last_one_idx)) % MOD
            if one_num > 0:
                res = (res + dfs(i + 1, zero_num, one_num - 1, last_zero_idx, i)) % MOD
            return res
        
        ans = dfs(0, zero, one, -1, -1)
        dfs.cache_clear()
        return ans  # 错误
    


class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        n = zero + one
        MOD = 1_000_000_007

        @cache
        def dfs(i: int, zero_num: int, one_num: int, last_zero_idx: int, last_one_idx: int):
            if i == n:
                return 1 
            res = 0

            if zero_num > 0 and (i - last_one_idx) <= limit:
                res = (res + dfs(i + 1, zero_num - 1, one_num, i, last_one_idx)) % MOD
            
            if one_num > 0 and (i - last_zero_idx) <= limit:
                res = (res + dfs(i + 1, zero_num, one_num - 1, last_zero_idx, i)) % MOD
            
            return res
        
        ans = dfs(0, zero, one, -1, -1)
        dfs.cache_clear()
        return ans  # 超时
    

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 1_000_000_007

        @cache
        def dfs(zero_num: int, one_num: int, last_zero_idx: int, last_one_idx: int):
            if zero_num == zero and one_num == one:
                return 1 
            res = 0

            i = zero_num + one_num
            if zero_num < zero and (i - last_one_idx) <= limit:
                res = (res + dfs(zero_num + 1, one_num, i, last_one_idx)) % MOD
            
            if one_num <one and (i - last_zero_idx) <= limit:
                res = (res + dfs(zero_num, one_num + 1, last_zero_idx, i)) % MOD
            
            return res
        
        ans = dfs(0, 0, -1, -1)
        dfs.cache_clear()
        return ans  # 炸内存
    

class Solution:
    # DP + 容斥原理
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 1_000_000_007
        
        # dp[i][j][0] 表示 i 个 0，j 个 1，且以 0 结尾的方案数
        # dp[i][j][1] 表示 i 个 0，j 个 1，且以 1 结尾的方案数
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # 初始化边界条件
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1
            
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # 填 0 的情况
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD
                if i > limit:
                    # 减去由于追加 0 导致连续 0 超过 limit 的非法情况
                    dp[i][j][0] = (dp[i][j][0] - dp[i - 1 - limit][j][1]) % MOD
                
                # 填 1 的情况
                dp[i][j][1] = (dp[i][j-1][0] + dp[i][j-1][1]) % MOD
                if j > limit:
                    # 减去由于追加 1 导致连续 1 超过 limit 的非法情况
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - 1 - limit][0]) % MOD

        ans = (dp[zero][one][0] + dp[zero][one][1]) % MOD
        return ans