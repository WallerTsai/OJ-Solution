from functools import cache


# 代码示例：返回 [low, high] 中的恰好包含 target 个 0 的数字个数
# 比如 digitDP(0, 10, 1) == 2
# 要点：我们统计的是 0 的个数，需要区分【前导零】和【数字中的零】，前导零不能计入，而数字中的零需要计入
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

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/discuss/post/tXLS3i/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution:
    def countFancy(self, l: int, r: int) -> int:
        def check(num: int):
            s = str(num)
            n = len(s)
            if n == 1:
                return True
            
            flag1 = flag2 = True
            for i in range(1, n):
                if s[i] >= s[i - 1]:
                    flag2 = False
                if s[i] <= s[i - 1]:
                    flag1 = False
            return flag1 or flag2
                
        def digitDP(low: int, high: int) -> int:
            STATE_INIT = 0      # 已经填了至多一个数（不含前导零）
            STATE_INC = 1       # 已填数字是严格递增的
            STATE_DEC = 2       # 已填数字是严格递减的
            STATE_BAD = 3       # 已填数字不是好数


            low_s = list(map(int, str(low)))
            high_s = list(map(int, str(high)))
            n = len(high_s)
            diff_lh = n - len(low_s)

            @cache
            def dfs(i: int, sums: int, pre: int, state: int, limit_low: bool, limit_high: bool) -> int:
                if i == n:
                    if state != STATE_BAD or check(sums):
                        return 1
                    return 0
                
                lo = low_s[i - diff_lh] if limit_low and i >= diff_lh else 0
                hi = high_s[i] if limit_high else 9

                res = 0
                d = lo
                if limit_low and i < diff_lh:
                    # 不填数字
                    res = dfs(i + 1, 0, 0, STATE_INIT, True, False)
                    d = 1

                for d in range(d, hi + 1):
                    nxt_sums = sums + d
                    nxt_pre = d

                    nxt_state = state
                    if state == STATE_INIT:
                        if pre > 0:
                            if d > pre:
                                nxt_state = STATE_INC
                            elif d < pre:
                                nxt_state = STATE_DEC
                            else:
                                nxt_state = STATE_BAD
                    elif state == STATE_INC:
                        if d <= pre:
                            nxt_state = STATE_BAD
                    elif state == STATE_DEC:
                        if d >= pre:
                            nxt_state = STATE_BAD

                    nxt_limit_low = limit_low and d == lo
                    nxt_limit_high = limit_high and d == hi

                    res += dfs(i + 1, nxt_sums, nxt_pre, nxt_state, nxt_limit_low, nxt_limit_high)

                return res
            ans = dfs(0, 0, 0, STATE_INIT, True, True)
            dfs.cache_clear()
            return ans
        
        return digitDP(l, r)
    

ans = Solution().countFancy(8, 9)
print(ans)


class Solution:
    # 群里大佬
    def countFancy(self, l: int, r: int) -> int:
        high = str(r)
        low = '0' * (len(high) - len(str(l))) + str(l)
        high = list(map(int, high))
        low = list(map(int, low))
        n = len(high)

        def check(sums):
            if 1 <= sums < 10:
                return 1
            a = list(map(int, str(sums)))
            return all(a[j] < a[j + 1] for j in range(len(a) - 1)) or all(a[j] > a[j + 1] for j in range(len(a) - 1))

        def f1(flag):
            from functools import cache # 如果在力扣外运行，记得加上这句导入
            @cache
            def dfs(i, pre, sums, isLimit, isLow):
                if i == n:
                    if pre == -1:
                        return 0
                    if flag == 0 or flag == 1:
                        # print('sums',sums)
                        if 1 <= sums < 10:
                            return 0
                        return int(not check(sums))

                    else:
                        # print('check',sums)
                        return int(check(sums))

                ans = 0
                lo = low[i] if isLow else 0
                hi = high[i] if isLimit else 9

                for d in range(lo, hi + 1):
                    if pre == -1 and d == 0:
                        ans += dfs(i + 1, -1, sums, isLimit and d == hi, isLow and d == lo)
                    else:
                        if pre == -1 or flag == 0 and d > pre or flag == 1 and d < pre or flag == 2:
                            ans += dfs(i + 1, d, sums + d, isLimit and d == hi, isLow and d == lo)
                return ans

            res = dfs(0, -1, 0, 1, 1)
            dfs.cache_clear()
            return res

        inc = f1(0)
        dec = f1(1)
        sums = f1(2)
        tot = inc + dec + sums
        return tot
    
    
class Solution:
    def countFancy(self, l: int, r: int) -> int:
        def check(num: int):
            s = str(num)
            n = len(s)
            if n == 1:
                return True
            
            flag1 = flag2 = True
            for i in range(1, n):
                if s[i] >= s[i - 1]:
                    flag2 = False
                if s[i] <= s[i - 1]:
                    flag1 = False
            return flag1 or flag2
                
        def digitDP(low: int, high: int) -> int:
            low_s = list(map(int, str(low)))
            high_s = list(map(int, str(high)))
            n = len(high_s)
            diff_lh = n - len(low_s)

            @cache
            def dfs(i: int, s: int, pre: int, flag: int, begin: int, limit_low: bool, limit_high: bool) -> int:
                if i == n:
                    if flag != -1:
                        return 1
                    if check(s):
                        return 1
                    return 0
                
                lo = low_s[i - diff_lh] if limit_low and i >= diff_lh else 0
                hi = high_s[i] if limit_high else 9

                res = 0
                d = lo

                for d in range(d, hi + 1):
                    nxt_pre = d
                    nxt_begin = begin or (d > 0)
                    if not begin and d == 0:
                        nxt_flag = -2
                        nxt_pre = 0
                    elif not begin and d > 0:
                        nxt_flag = 0
                    else:
                        if flag == -1:
                            nxt_flag = -1
                        elif flag == 0:
                            if d > pre:
                                nxt_flag = 1
                            elif d < pre:
                                nxt_flag = 2
                            else:
                                nxt_flag = -1
                        elif flag == 1:
                            nxt_flag = 1 if d > pre else -1
                        elif flag == 2:
                            nxt_flag = 2 if d < pre else -1
                    res += dfs(i + 1,
                            s + d,
                            nxt_pre,
                            nxt_flag,
                            nxt_begin,
                            limit_low and d == lo,
                            limit_high and d == hi)

                return res
            ans = dfs(0, 0, -1, -2, False, True, True)
            dfs.cache_clear()
            return ans
        
        return digitDP(l, r)