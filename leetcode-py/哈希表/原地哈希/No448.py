from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for x in nums:
            y = abs(x) - 1
            nums[y] = -abs(nums[y])
        return [i + 1 for i, x in enumerate(nums) if x > 0]




