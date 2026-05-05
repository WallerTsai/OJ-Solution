from functools import cache


def digitDP(low: int, high: int, target: int) -> int:
    low_s = list(map(int, str(low)))
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
        if limit_low and i < diff_lh:
            res = dfs(i + 1, cnt0, True, False)
            d = 1
        for d in range(d, hi + 1):
            res += dfs(i + 1,
                       cnt0 + (1 if d == 0 else 0),
                       limit_low and d == lo,
                       limit_high and d == hi)

        return res

    return dfs(0, 0, True, True)

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        low_s = [1]
        high_s = list(map(int, str(n)))
        n = len(high_s)
        diff_lh = n - len(low_s)

        @cache
        def dfs(i: int, mask: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1
            
            lo = low_s[i - diff_lh] if limit_low and i >= diff_lh else 0
            hi = high_s[i] if limit_high else 9

            res = 0
            d = lo
            if limit_low and i < diff_lh:
                res = dfs(i + 1, mask, True, False)
                d = 1
            for d in range(d, hi + 1):
                if mask >> d & 1 == 0:
                    res += dfs(i + 1, 
                           mask | (1 << d),
                           limit_low and d == lo,
                           limit_high and d == hi
                           )

            return res
        
        ans = dfs(0, 0, True, True)
        dfs.cache_clear()

        return ans