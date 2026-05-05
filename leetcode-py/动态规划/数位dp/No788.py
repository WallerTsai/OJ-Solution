from functools import cache


class Solution:
    def rotatedDigits(self, n: int) -> int:
        check = [0, 0, 1, -1, -1, 1, 1, -1, 0, 1]

        ans = 0
        for i in range(1, n + 1):
            num = [int(digit) for digit in str(i)]
            valid, diff = True, False
            for digit in num:
                if check[digit] == -1:
                    valid = False
                elif check[digit] == 1:
                    diff = True
            if valid and diff:
                ans += 1
        
        return ans

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
class Solution:
    def rotatedDigits(self, n: int) -> int:
        check = [0, 0, 1, -1, -1, 1, 1, -1, 0, 1]
        low_s = [1]
        high_s = list(map(int, str(n)))
        n = len(high_s)
        diff_lh = n - len(low_s)

        @cache
        def dfs(i: int, flag: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1 if flag else 0
            
            lo = low_s[i - diff_lh] if limit_low and i >= diff_lh else 0
            hi = high_s[i] if limit_high else 9

            res = 0
            d = lo
            if limit_low and i < diff_lh:
                res = dfs(i + 1, flag, True, False)
                d = 1
            for d in range(d, hi + 1):
                if check[d] != -1:
                    res += dfs(i + 1, 
                           flag or check[d] == 1,
                           limit_low and d == lo,
                           limit_high and d == hi
                           )

            return res
        
        ans = dfs(0, False, True, True)
        dfs.cache_clear()

        return ans
