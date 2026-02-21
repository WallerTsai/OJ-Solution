from functools import cache
from typing import List


class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        @cache
        def dfs(i, t):
            if i < 0:
                return 0
            
            # 增大
            res = dfs(i - 1, 0) + max(k - nums[i], 0)
            # 不增大
            if t < 2:
                res = min(res, dfs(i - 1, t + 1))
            return res
        
        ans = dfs(len(nums) - 1, 0)
        dfs.cache_clear()
        return ans
        
class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        f0 = f1 = f2 = 0
        for num in nums:
            inc = f0 + max(k - num, 0)
            f0 = min(inc, f1)
            f1 = min(inc, f2)
            f2 = inc
        return f0   # 67ms
