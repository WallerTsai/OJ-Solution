
from functools import cache


def digitDP(low: int, high: int, target: int) -> int:
    # 灵神模板
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

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        # 底值未解决

        def digitDP(low, high) -> int:
            if high_s < 100:
                return 0
            low_s = list(map(int, str(low)))
            high_s = list(map(int, str(high_s)))
            n = len(high_s)
            diff_lh = n - len(low_s)

            @cache
            def dfs(i, cnt, p2, p1, limit_low: bool, limit_high: bool):
                if i == n:
                    return cnt
                
                lo = low_s[i - diff_lh] if limit_low and i >= diff_lh else 0
                hi = high_s[i] if limit_high else 9

                res = 0
                for d in range(lo, hi + 1):
                    if p1 == -1:
                        if d == 0:
                            res += dfs(i + 1, 0, -1, -1, limit_low and (d == lo), limit_high and (d == hi))
                        else:
                            res += dfs(i + 1, 0, -1, d, limit_low and (d == lo), limit_high and (d == hi))
                    elif p2 == -1:
                        res += dfs(i + 1, 0, p1, d, limit_low and (d == lo), limit_high and (d == hi))
                    else:
                        temp = 0
                        if p1 > p2 and p1 > d:
                            temp = 1
                        elif p1 < p2 and p1 < d:
                            temp = 1
                        res += dfs(i + 1, cnt + temp, p1, d, limit_low and (d == lo), limit_high and (d == hi))
                return res

            return dfs(0, 0, -1, -1, True, True)
        
        return digitDP(num1 - 1, num2)

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        # 底值未解决
        # 利用
        def digitDP(high) -> int:
            if high < 100:
                return 0
            high = list(map(int, str(high)))
            lenght = len(high)

            @cache
            def dfs(i, cnt, p2, p1, limit_low: bool, limit_high: bool):
                if i == lenght:
                    return cnt
                
                lo = 0
                hi = high[i] if limit_high else 9

                res = 0
                for d in range(lo, hi + 1):
                    if p1 == -1:
                        if d == 0:
                            res += dfs(i + 1, 0, -1, -1, False, limit_high and (d == hi))
                        else:
                            res += dfs(i + 1, 0, -1, d, False, limit_high and (d == hi))
                    elif p2 == -1:
                        res += dfs(i + 1, 0, p1, d, False, limit_high and (d == hi))
                    else:
                        temp = 0
                        if p1 > p2 and p1 > d:
                            temp = 1
                        elif p1 < p2 and p1 < d:
                            temp = 1
                        res += dfs(i + 1, cnt + temp, p1, d, False, limit_high and (d == hi))
                return res

            return dfs(0, 0, -1, -1, True, True)
        
        return digitDP(num2) - digitDP(num1 - 1)
    
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        # 底值未解决

        def digitDP(low, high) -> int:
            if high < 100:
                return 0
            low_s = list(map(int, str(low)))
            high_s = list(map(int, str(high)))
            n = len(high_s)
            diff_lh = n - len(low_s)

            @cache
            def dfs(i, cnt, p2, p1, limit_low: bool, limit_high: bool):
                if i == n:
                    return cnt
                
                lo = low_s[i - diff_lh] if limit_low and i >= diff_lh else 0
                hi = high_s[i] if limit_high else 9

                res = 0
                for d in range(lo, hi + 1):
                    if p1 == -1:
                        if d == 0:
                            res += dfs(i + 1, 0, -1, -1, limit_low and (d == lo), limit_high and (d == hi))
                        else:
                            res += dfs(i + 1, 0, -1, d, limit_low and (d == lo), limit_high and (d == hi))
                    elif p2 == -1:
                        res += dfs(i + 1, 0, p1, d, limit_low and (d == lo), limit_high and (d == hi))
                    else:
                        temp = 0
                        if p1 > p2 and p1 > d:
                            temp = 1
                        elif p1 < p2 and p1 < d:
                            temp = 1
                        res += dfs(i + 1, cnt + temp, p1, d, limit_low and (d == lo), limit_high and (d == hi))
                return res

            return dfs(0, 0, -1, -1, True, True)
        
        return digitDP(num1, num2)
