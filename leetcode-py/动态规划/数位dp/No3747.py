from functools import cache


class Solution:
    def countDistinct(self, n: int) -> int:
        # n = XXXX
        # XXX0
        # XX0N  
        # X0NN

        ans = 1
        while n:
            a, b = divmod(n, 10)
            if b:
                ans *= b
            elif a != 0 and b == 0:
                ans *= 9
            n = a
        
        return ans  # 错误


class Solution:
    # 数位DP
    def countDistinct(self, n: int) -> int:
        s = list(map(int,str(n)))
        m = len(s)
        if m == 1:
            return n

        @cache
        def dfs(i: int, limit_high: bool) -> int:
            if i == m:
                return 1 
            
            hi = s[i] if limit_high else 9
            res = 0
            for d in range(1, hi + 1):
                res += dfs(i + 1, limit_high and d == hi)
            return res

        ans = 0
        for i in range(1, m - 1):
            ans += pow(9, i)

        return ans + dfs(0, True)   # 11ms



class Solution:
    # 灵神
    def countDistinct(self, n: int) -> int:
        s = str(n)
        m = len(s)

        # 计算长度小于 m 的不含 0 的整数个数
        # 9 + 9^9 + ... + 9^(m-1) = (9^m - 9) / 8
        pow9 = 9 ** m
        ans = (pow9 - 9) // 8

        # 计算长度恰好等于 m 的不含 0 的整数个数
        for i, d in enumerate(s):
            if d == '0':  # 只能填 0，不合法，跳出循环
                break
            # 这一位填 1 到 d-1，后面的数位可以随便填 1 到 9
            v = int(d) - 1
            if i == m - 1:
                v += 1  # 最后一位可以等于 d
            pow9 //= 9
            ans += v * pow9

        return ans  # 4ms
    

class Solution:
    # 数位DP
    
    def countDistinct(self, n: int) -> int:
        s = list(map(int,str(n)))
        m = len(s)

        @cache
        def dfs(i: int, limit_low: bool, limit_high: bool) -> int:
            if i == m:
                return 1 
            
            lo = 1 if limit_low else 0
            hi = s[i] if limit_high else 9
            res = 0
            for d in range(lo, hi + 1):
                res += dfs(i + 1, limit_low or d != 0, limit_high and d == hi)
            return res

        return dfs(0, False, True) - 1  # 35ms
    

class Solution:
    # 数位DP
    def countDistinct(self, n: int) -> int:
        def digitDP(low: int, high: int, target: int) -> int:
            low_s = list(map(int, str(low)))  # 避免在 dfs 中频繁调用 int()
            high_s = list(map(int, str(high)))
            n = len(high_s)
            diff_lh = n - len(low_s)

            @cache
            def dfs(i: int, cnt0: int, limit_low: bool, limit_high: bool) -> int:
                if cnt0 > target:
                    return 0  # 不合法
                if i == n:
                    return 1 if cnt0 == target else 0

                lo = low_s[i - diff_lh] if limit_low and i >= diff_lh else 0
                hi = high_s[i] if limit_high else 9

                res = 0
                d = lo
                # 通过 limit_low 和 i 可以判断能否不填数字，无需 is_num 参数
                # 如果前导零不影响答案，去掉这个 if block
                if limit_low and i < diff_lh:
                    # 不填数字，上界不受约束
                    res = dfs(i + 1, cnt0, True, False)
                    d = 1
                for d in range(d, hi + 1):
                    res += dfs(i + 1,
                            cnt0 + (1 if d == 0 else 0),  # 统计 0 的个数
                            limit_low and d == lo,
                            limit_high and d == hi)

                # res %= MOD
                return res

            return dfs(0, 0, True, True)
        
        return digitDP(1, n, 0) # 47ms
    


class Solution:
    # deepseek 三发wa后正确
    def countDistinct(self, n: int) -> int:
        s = str(n)
        m = len(s)
        total = 0
        
        # 长度小于 m 的所有不含零数字
        for L in range(1, m):
            total += 9 ** L
        
        # 长度等于 m 的不含零数字且 ≤ n
        from functools import lru_cache
        
        @lru_cache(None)
        def dp(pos, tight):
            if pos == m:
                return 1
            total = 0
            up = int(s[pos]) if tight else 9
            for dig in range(1, up + 1):
                total += dp(pos + 1, tight and dig == up)
            return total
        
        total += dp(0, True)
        return total