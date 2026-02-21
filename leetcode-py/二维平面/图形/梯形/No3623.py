from collections import Counter
from typing import List


class Solution:
    # 枚举右, 维护左
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 1_000_000_007
        cnt = Counter(p[1] for p in points)  # 统计每一行（水平线）有多少个点
        ans = s = 0
        for c in cnt.values():
            k = c * (c - 1) // 2
            ans += s * k
            s += k
        return ans % MOD    #70ms


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 1_000_000_007
        cnt = Counter(p[1] for p in points)
        ans = pre_num = 0
        for c in cnt.values():
            num = c * (c - 1) // 2
            ans = (ans + pre_num * num) % MOD
            pre_num += num
        return ans  # 71ms
