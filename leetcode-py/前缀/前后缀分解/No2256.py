from math import inf
from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        suf = sum(nums)
        ans = pre = 0
        diff = inf
        for i, x in enumerate(nums):
            pre += x
            suf -= x
            if i < n - 1:
                d = pre // (i + 1) - suf // (n - i - 1)
            else:
                d = pre // (i + 1)
            if abs(d) < diff:
                diff = abs(d)
                ans = i
            if d == 0:
                break
        return ans  # 59ms