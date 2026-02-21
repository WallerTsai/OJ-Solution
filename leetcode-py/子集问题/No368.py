from functools import cache
from typing import List

# 灵神
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        from_ = [-1] * n

        @cache
        def dfs(i: int) -> int:
            res = 0
            for j in range(i):
                if nums[i] % nums[j]:
                    continue
                f = dfs(j)
                if f > res:
                    res = f
                    from_[i] = j
            return res + 1
        
        max_length = max_i = 0 # max_i 记录最后最大的子集下标
        for i in range(n):
            f = dfs(i)
            if f > max_length:
                max_length = f
                max_i = i

        path = []
        while max_i >= 0:
            path.append(nums[i])
            max_i = from_[i]

        return path


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        from_ = [-1] * n
        dp = [0] * n
        max_i = 0

        for i,x in enumerate(nums):
            for j in range(i):
                if x % nums[j] == 0 and dp[j] > dp[i]:
                    dp[i] = dp[j]
                    from_[i] = j
            dp[i] += 1
            if dp[i] > dp[max_i]:
                max_i = i

        path = []
        while max_i >= 0:
            path.append(nums[max_i])
            max_i = from_[max_i]

        return path

