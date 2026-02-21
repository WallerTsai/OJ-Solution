from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = sorted(x ** 2 for x in nums)
        n = len(nums) // 2
        return sum(nums[n:]) - sum(nums[:n])