from itertools import accumulate
from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        x = 0
        for num in nums:
            x = x * 2 + num
            if x % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)

        return ans  # 135ms


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        x = 0
        for i, bit in enumerate(nums):
            x = (x << 1 | bit) % 5  # 中途取模, 数太大会影响效率
            if x == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans  # 4ms
            