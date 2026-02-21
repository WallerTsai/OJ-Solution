from functools import cache

class Solution:
    def countBalanced(self, low: int, high: int) -> int:

        def calc(x: int):
            s = list(map(int, str(x)))
            m = len(s)

            @cache
            def dfs(i: int, limit_high: bool, diff: int) -> int:
                if i == m:
                    return 1 if diff == 0 else 0
                
                hi = s[i] if limit_high else 9
                res = 0
                for d in range(hi + 1):
                    res += dfs(i + 1,limit_high and d == hi, diff + (d if i % 2 else -d))
                return res
            
            res = dfs(0, True, 0)
            dfs.cache_clear()
            return res
        
        return calc(high) - calc(low - 1)   # 956ms
    

class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        # 最小的满足要求的数是 11
        if high < 11:
            return 0

        low = max(low, 11)
        low_s = list(map(int, str(low)))  # 避免在 dfs 中频繁调用 int()
        high_s = list(map(int, str(high)))
        n = len(high_s)
        diff_lh = n - len(low_s)

        @cache
        def dfs(i: int, diff: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1 if diff == 0 else 0

            lo = low_s[i - diff_lh] if limit_low and i >= diff_lh else 0
            hi = high_s[i] if limit_high else 9

            res = 0
            start = lo

            # 通过 limit_low 和 i 可以判断能否不填数字，无需 is_num 参数
            if limit_low and i < diff_lh:
                # 不填数字，上界不受约束
                res = dfs(i + 1, diff, True, False)
                start = 1  # 下面填数字，至少从 1 开始填

            for d in range(start, hi + 1):
                res += dfs(i + 1,
                           diff + (d if i % 2 else -d),
                           limit_low and d == lo,
                           limit_high and d == hi)

            return res

        return dfs(0, 0, True, True)