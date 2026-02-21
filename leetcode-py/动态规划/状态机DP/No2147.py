from functools import cache


class Solution:
    # 记忆化搜索
    def numberOfWays(self, corridor: str) -> int:
        MOD  = 1_000_000_007
        n = len(corridor)

        @cache
        def dfs(i: int, k: int):
            if i >= n:
                return 1 if k == 2 else 0
            
            k += 1 if corridor[i] == "S" else 0

            if k > 2:
                return 0
            
            # 不分割
            ans = dfs(i + 1, k) % MOD
            # 分割
            if k == 2:
                ans = (ans + dfs(i + 1, 0)) % MOD

            return ans
        
        ans = dfs(0, 0)
        dfs.cache_clear()
        return ans  # 4335ms
    
# nk = k + 1 if corridor[i] == 'S' else k
# 如果 nk > 2:
#     dp[i][k] = 0
# 否则:
#     dp[i][k] = dp[i+1][nk] + (dp[i+1][0] if nk == 2 else 0)

class Solution:
    # DP
    def numberOfWays(self, corridor: str) -> int:
        MOD  = 1_000_000_007
        n = len(corridor)
        dp = [[0] * 3 for _ in range(n + 1)]
        dp[n][2] = 1

        for i in range(n - 1, -1, -1):
            for k in range(3):
                nk = k + (1 if corridor[i] == "S" else 0)
                if nk > 2:
                    dp[i][k] = 0
                    continue
                # 不分割情况
                res = dp[i + 1][nk]
                # 分割
                if nk == 2:
                    res = (res + dp[i + 1][0]) % MOD

                dp[i][k] = res

        return dp[0][0] # 2915ms
    
class Solution:
    # DP 交替数组
    def numberOfWays(self, corridor: str) -> int:
        MOD  = 1_000_000_007
        n = len(corridor)
        dp = [0] * 3
        dp[2] = 1

        for i in range(n - 1, -1, -1):
            new_dp = [0] * 3
            for k in range(3):
                nk = k + (1 if corridor[i] == "S" else 0)
                if nk > 2:
                    new_dp[k] = 0
                    continue
                res = dp[nk]
                if nk == 2:
                    res = (res + dp[0]) % MOD
                new_dp[k] = res
            dp = new_dp
        return dp[0]    # 2116ms
    
class Solution:
    # DP
    def numberOfWays(self, corridor: str) -> int:
        MOD  = 1_000_000_007
        n = len(corridor)
        dp = [0] * 3
        dp[2] = 1
        
        for i in range(n - 1, -1, -1):
            for k in range(1, -1, -1):
                nk = k + (1 if corridor[i] == "S" else 0)
                dp[k] = dp[nk]
                if nk == 2:
                    dp[k] = (dp[k] + dp[0]) % MOD
            
            k = 2
            nk = k + (1 if corridor[i] == "S" else 0)
            if nk > 2:
                dp[k] = 0
        
        return dp[0]    # 错误

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 1_000_000_007
        # 状态：a=dp[0], b=dp[1], c=dp[2]
        a, b, c = 0, 0, 1
        
        for i in range(len(corridor) - 1, -1, -1):
            if corridor[i] == "S":
                # new_a = b
                # new_b = c + a
                # new_c = 0
                a, b, c = b, (c + a) % MOD, 0
            else:  # corridor[i] == "P"
                # new_a = a
                # new_b = b
                # new_c = c + a
                a, b, c = a, b, (c + a) % MOD
                
        return a % MOD  # 357ms

class Solution:
    # 从左往右 状态机
    def numberOfWays(self, corridor: str) -> int:
        MOD  = 1_000_000_007
        n = len(corridor)
        dp = [[0] * 3 for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(n):
            if corridor[i] == "P":
                dp[i + 1][1] = dp[i][1]
                dp[i + 1][2] = dp[i][2]

                dp[i + 1][0] = (dp[i][0] + dp[i][2]) % MOD
            else:
                dp[i + 1][0] = 0
                dp[i + 1][1] = dp[i][0]
                dp[i + 1][2] = dp[i][1]
                # 当 k = 2 时候， nk = 3 必须划分，转移下一个状态到 k = 1
                dp[i + 1][1] = (dp[i + 1][1] + dp[i][2]) % MOD
        return dp[n][2] # 1964ms
    
class Solution:
    # 状态机
    def numberOfWays(self, corridor: str) -> int:
        MOD = 1_000_000_007
        
        dp = [1, 0, 0]  # dp[0], dp[1], dp[2]
        
        for ch in corridor:
            new_dp = [0, 0, 0]
            if ch == "P":
                new_dp[0] = (dp[0] + dp[2]) % MOD
                new_dp[1] = dp[1]
                new_dp[2] = dp[2]
            else:
                new_dp[0] = 0
                new_dp[1] = (dp[0] + dp[2]) % MOD
                new_dp[2] = dp[1]
            
            dp = new_dp
        
        return dp[2] % MOD  # 612ms
    

class Solution:
    # 数学
    def numberOfWays(self, corridor: str) -> int:
        MOD = 1_000_000_007
        ans = 1
        cnt_s = last_s_idx = 0

        for i, ch in enumerate(corridor):
            if ch == "S":
                cnt_s += 1
                if cnt_s >= 3 and cnt_s % 2:
                    ans = ans * (i - last_s_idx) % MOD
                last_s_idx = i

        if cnt_s == 0 or cnt_s % 2:
            return 0
        return ans
    

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # 记录所有座位的下标
        pos = [i for i, char in enumerate(corridor) if char == 'S']
        
        # 没有座位，或座位总数不是偶数
        if not pos or len(pos) % 2:
            return 0
        
        ans, MOD = 1, 10 ** 9 + 7
        
        # 每一对 “相邻组” 之间的间隔
        for i in range(2, len(pos), 2):
            # "上一组" 的第二个座位和"下一组" 的第一个座位之间
            ans *= pos[i] - pos[i - 1]
            ans %= MOD
        
        return ans
