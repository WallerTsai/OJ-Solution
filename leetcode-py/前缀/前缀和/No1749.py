from itertools import accumulate
from typing import List


class Solution:
    # 动态规划
    # 灵神
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = f_max = f_min = 0
        for x in nums:
            f_max = max(f_max, 0) + x
            f_min = min(f_min, 0) + x
            ans = max(ans, f_max, -f_min)
        return ans


class Solution:
    # 前缀和
    # 灵神
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        s = list(accumulate(nums, initial=0))  # nums 的前缀和
        return max(s) - min(s)
