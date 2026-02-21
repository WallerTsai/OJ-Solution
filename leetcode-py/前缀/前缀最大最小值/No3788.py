from math import inf
from typing import List

fmin = lambda x, y : y if x > y else x
fmax = lambda x, y : x if x > y else y
class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        suffix_min = nums.copy()
        for i in range(n - 2, -1, -1):
            suffix_min[i] = fmin(suffix_min[i], suffix_min[i + 1])

        pre = 0
        ans = -inf
        for i in range(n - 1):
            pre += nums[i]
            ans = fmax(ans, pre - suffix_min[i + 1])

        return ans
