from math import inf
from typing import List


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-inf] * n
        dp[0] = 0
        for i, x in enumerate(nums):
            for j in range(i + 1, n):
                y = nums[j]
                if abs(y - x) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
        return -1 if dp[n - 1] == -inf else dp[n- 1]


