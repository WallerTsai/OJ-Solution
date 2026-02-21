from functools import cache
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()
        def dfs(n):
            if n == 0:
                nonlocal res
                res += 1
                return
            for i in nums:
                if i > n:
                    break
                dfs(n-i)
        dfs(target)
        return res  # 超时
        # 这样子写不利于记忆化搜索：最后放回的是个数，与哪些数在里面无关

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(n:int):
            if n == 0:
                return 1
            res = sum(dfs(n-x) for x in nums if x <= n)
            return res
        return dfs(target)
    
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1,target+1):
            dp[i] = sum(dp[i-x] for x in nums if x <= i)
        return dp[target]