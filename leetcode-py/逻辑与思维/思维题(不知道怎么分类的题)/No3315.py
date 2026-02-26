from typing import List


class Solution:
    # 灵神
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i, x in enumerate(nums):
            if x == 2:
                nums[i] = -1
            else:
                nums[i] ^= ((x + 1) & ~x) >> 1
        return nums