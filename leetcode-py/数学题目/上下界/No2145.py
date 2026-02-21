from itertools import accumulate
from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        l, h = lower, upper
        cur = 0
        for d in differences:
            cur += d
            l = max(l,lower - cur)
            h = min(h,upper - cur)
        ans = h - l + 1
        return ans if ans >=0 else 0


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        l, h = lower, upper
        for d in accumulate(differences):
            l = max(l,lower - d)
            h = min(h,upper - d)
        ans = h - l + 1
        return ans if ans >=0 else 0
    
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_s = min(accumulate(differences, initial=0))  # 前缀和的最小值
        max_s = max(accumulate(differences, initial=0))  # 前缀和的最大值
        return max(upper - lower - max_s + min_s + 1, 0)