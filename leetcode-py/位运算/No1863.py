from functools import cache
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        def dfs(i:int,path:int):
            if i == n:
                nonlocal ans
                ans += path
                return
            dfs(i + 1,path)
            dfs(i + 1,path ^ nums[i])

        dfs(0,0)

        return ans