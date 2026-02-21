from math import inf
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        pre_r = -inf
        for l, r in intervals:
            if l >= pre_r:
                ans += 1
                pre_r = r
        return len(intervals) - ans