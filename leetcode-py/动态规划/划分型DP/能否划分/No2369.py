from functools import cache
from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        @cache
        def dfs(i: int):
            if i < 0:
                return True
            if i >= 1 and nums[i] == nums[i - 1] and dfs(i - 2):
                return True
            elif i >= 2 and (nums[i] == nums[i - 1] == nums[i - 2] or nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2) and dfs(i - 3):
                return True
            return False
        ans = dfs(len(nums) - 1)
        dfs.cache_clear()
        return ans
    

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [True] + [False] * len(nums)
        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i - 1] and dp[i - 1]:
                dp[i + 1] = True
            elif i >= 2 and (nums[i] == nums[i - 1] == nums[i - 2] or nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2) and dp[i - 2]:
                dp[i + 1] = True
        return dp[-1]



