from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        total = sum(set(num for num in nums if num > 0))
        return total if total else max(nums)