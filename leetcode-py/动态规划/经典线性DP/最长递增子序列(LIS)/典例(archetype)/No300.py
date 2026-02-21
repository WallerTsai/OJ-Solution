from bisect import bisect_left
from functools import cache
from math import inf
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(i:int,length:int,pre:int):
            if i == n:
                nonlocal ans
                ans = max(ans ,length)
                return
            if nums[i] > pre:
                dfs(i + 1, length + 1,pre = nums[i])
            dfs(i + 1, length, pre)

        ans = 0
        dfs(0,0,-inf)
        return ans  # 超时

class Solution:
    # 灵神
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j))
            return res + 1  # 加一提到循环外面
        return max(dfs(i) for i in range(len(nums)))    # 2677ms
    

class Solution:
    # 灵神
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[:i]):
                if x > y:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += 1
        return max(dp)  # 2187ms
    
class Solution:
    # 灵神
    def lengthOfLIS(self, nums: List[int]) -> int:
        g = []
        for x in nums:
            j = bisect_left(g, x)
            if j == len(g):  # >=x 的 g[j] 不存在
                g.append(x)
            else:
                g[j] = x
        return len(g)
