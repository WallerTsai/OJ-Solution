from collections import Counter
from math import inf
from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        a = [0] * (max(power) + 1)
        for p in power:
            a[p] += p

        a1 = a2 = a3 = 0
        for x in a:
            temp = a3
            a3 = max(a1 + x,a2,a3)
            a1,a2 = a2,temp
        return a3    # 爆内存

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        a = sorted(cnt.keys())

        a1 = a2 = a3 = 0
        i1 = i2 = i3 = -inf
        ans = 0
        for x in a:  
            dp = a1 + x * cnt[x]

            if x - 2 > i2:
                dp = max(dp, a2 + x * cnt[x])

            if x - 2 > i3:
                dp = max(dp, a3 + x * cnt[x])

            ans = max(ans, dp)
            a1, a2, a3 = a2, a3, ans
            i1, i2, i3 = i2, i3, x

        return ans  # 588ms

class Solution:
    # 灵神
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        a = sorted(cnt.keys())
        f = [0] * (len(a) + 1)
        j = 0
        for i, x in enumerate(a):
            while a[j] < x - 2:
                j += 1
            f[i + 1] = max(f[i], f[j] + x * cnt[x])
        return f[-1]


fun = Solution()
fun.maximumTotalDamage([1,1,2,2,3,4])
