from collections import Counter, defaultdict
from functools import cache


class Solution:
    def sum_digit(self, n: int) -> int:
        str_n = str(n)
        return sum(int(c) for c in str_n)
    
    def countLargestGroup(self, n: int) -> int:
        ans = max_cnt = 0
        cnt = Counter()
        for i in range(1,n + 1):
            sum_num = self.sum_digit(i)
            cnt[sum_num] += 1
            if cnt[sum_num] > max_cnt:
                max_cnt = cnt[sum_num]
                ans = 1
            elif cnt[sum_num] == max_cnt:
                ans += 1
        return ans
    

class Solution:
    # 数位DP
    def countLargestGroup(self, n: int) -> int:
        s = list(map(int,str(n)))
        m = len(s)

        @cache
        def dfs(i: int, left: int, limit_high: bool) -> int:
            if i == m:
                return 1 if left == 0 else 0
            
            hi = s[i] if limit_high else 9
            res = 0
            for d in range(min(hi,left) + 1):
                res += dfs(i + 1, left - d, limit_high and d == hi)
            return res

        ans = max_cnt = 0
        for target in range(1, m * 9 + 1):
            cnt = dfs(0,target, True)
            if cnt > max_cnt:
                max_cnt = cnt
                ans = 1
            elif cnt == max_cnt:
                ans += 1
        return ans