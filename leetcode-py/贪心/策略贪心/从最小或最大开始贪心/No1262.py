from functools import cache
from math import inf
from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        s = sum(nums)
        if s % 3 == 0:
            return s
        
        a1 = sorted(x for x in nums if x % 3 == 1)
        a2 = sorted(x for x in nums if x % 3 == 2)

        if s % 3 == 1:
            ans = s - a1[0] if a1 else 0
            if len(a2) > 1:
                ans = max(ans,s - a2[0] - a2[1])
        else:
            ans = s - a2[0] if a2 else 0
            if len(a1) > 1:
                ans = max(ans,s - a1[0] - a1[1])

        return ans 
    
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        s = sum(nums)
        if s % 3 == 0:
            return s
        a1 = sorted(x for x in nums if x % 3 == 1)
        a2 = sorted(x for x in nums if x % 3 == 2)
        if s % 3 == 2:
            a1, a2 = a2, a1
        ans = s - a1[0] if a1 else 0
        if len(a2) > 1:
            ans = max(ans, s - a2[0] - a2[1])
        return ans # 15ms
    

# 以下是递归递推

class Solution:
    def maxSumDivThree(self, nums:List[int]) -> int:
        @ cache
        def dfs(i:int,remainder:int) -> int:
            if i < 0:
                return -inf if remainder else 0
            return max( dfs(i-1,remainder),dfs(i-1,(remainder + nums[i]) % 3) + nums[i] )
        return dfs(len(nums) - 1, 0) # 347ms

class Solution:
    def maxSumDivThree(self, nums:List[int]) -> int:
        dp = [[-inf] * 3 for _ in range(len(nums) + 1)]
        dp[0][0] = 0
        for i,x in enumerate(nums):
            for j in range(3):
                dp[i+1][j] = max(dp[i][j],dp[i][(j + x) % 3] + x)
        return dp[-1][0] # 154ms

class Solution:
    # 滚动数组
    def maxSumDivThree(self, nums: List[int]) -> int:
        f = [[-inf] * 3 for _ in range(2)]
        f[0][0] = 0
        for i, x in enumerate(nums):
            for j in range(3):
                f[(i + 1) % 2][j] = max(f[i % 2][j], f[i % 2][(j + x) % 3] + x)
        return f[len(nums) % 2][0]

class Solution:
    def maxSumDivThree(self, nums:List[int]) -> int:
        dp = [0,-inf,-inf]
        for x in nums:
            next_dp = [-inf,-inf,-inf]
            for j in range(3):
                next_dp[j] = max(dp[j],dp[(j + x) % 3] + x)
            dp = next_dp
        return dp[0]    #  111ms
