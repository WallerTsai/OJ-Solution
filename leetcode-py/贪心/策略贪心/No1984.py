from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        return min(nums[i] - nums[i - k + 1] for i in range(k - 1, n))