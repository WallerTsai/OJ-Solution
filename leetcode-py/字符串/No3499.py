from collections import defaultdict
from itertools import groupby, pairwise
from math import inf


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        s = list("1" + s + "1")
        cnt = defaultdict(list)
        max_ = -1
        max_l = max_r = 0
        num_1 = 0
        
        for i, c in enumerate(s):
            if c == "0":
                cnt["0"].append(i)

        for a,b in pairwise(cnt["0"]):
            if a + 1 == b:
                continue
            temp = b - a - 1
            while s[a-1] == "0":
                a -= 1
            while s[b+1] == "0":
                b += 1
            if b - a + 1 - temp > max_:
                max_ = b - a + 1 - temp
                max_l = a
                max_r = b

        for i in range(max_l,max_r + 1):
            s[i] = "1"

        return sum(1 for c in s if c == "1") - 2


class Solution:
    # 灵神一次遍历
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total1 = mx = cnt = 0
        pre0 = -inf
        for i, b in enumerate(s):
            cnt += 1
            if i == len(s) - 1 or b != s[i + 1]:  # i 是这一段的末尾
                if b == '1':
                    total1 += cnt
                else:
                    mx = max(mx, pre0 + cnt)
                    pre0 = cnt
                cnt = 0
        return total1 + mx

class Solution:
    # 灵神
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total1 = mx = 0
        pre0 = -inf
        for b, group in groupby(s):
            cnt = len(list(group))
            if b == '1':
                total1 += cnt
            else:
                mx = max(mx, pre0 + cnt)
                pre0 = cnt
        return total1 + mx

fun = Solution()
fun.maxActiveSectionsAfterTrade(s="00100111011")