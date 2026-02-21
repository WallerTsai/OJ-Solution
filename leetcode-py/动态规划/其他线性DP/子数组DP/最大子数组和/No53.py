from math import inf
from typing import List


class Solution:
    # 前缀和
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf
        MIN = cur_sum = 0
        for x in nums:
            cur_sum += x
            ans = max(ans,cur_sum-MIN)
            MIN = min(MIN,cur_sum)
        return ans

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf
        cur_sum = 0
        for x in nums:
            if cur_sum > 0:
                cur_sum += x
            else:
                cur_sum = x
            ans = max(ans,cur_sum)
        return ans
    
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], 0) + nums[i]
        return max(dp)
    

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf  # 注意答案可以是负数，不能初始化成 0
        f = 0
        for x in nums:
            f = max(f, 0) + x
            ans = max(ans, f)
        return ans