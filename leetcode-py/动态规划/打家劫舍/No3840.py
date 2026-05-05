from typing import List

class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(1, n):
            if colors[i] != colors[i - 1]:
                dp[i + 1] = dp[i] + nums[i]
            else:
                dp[i + 1] = max(dp[i - 1] + nums[i], dp[i])
        return dp[-1]
    

class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        for i, x in enumerate(nums):
            if colors[i] != colors[i - 1]:
                dp[i + 1] = dp[i] + x
            else:
                dp[i + 1] = max(dp[i - 1] + x, dp[i])
        return dp[-1]