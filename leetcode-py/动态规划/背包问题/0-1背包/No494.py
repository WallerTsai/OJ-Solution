from functools import cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def dfs(i: int, t: int):
            if i == n:
                return t == target
            return dfs(i + 1, t + nums[i]) + dfs(i + 1, t - nums[i])

        ans = dfs(0, 0)
        dfs.cache_clear()
        return ans


