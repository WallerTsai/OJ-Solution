from itertools import accumulate
from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        max_end = max(e for _, e in nums)
        diff = [0] * (max_end+2)
        for s, e in nums:
            diff[s] += 1
            diff[e+1] -= 1

        return sum(s>0 for s in accumulate(diff))