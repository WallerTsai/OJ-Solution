# 贪心6
# 难度简单

from typing import List
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)

        for i in range(len(nums)):
            if sum(nums[0:i+1]) > sum(nums[i+1:]):
                return nums[0:i+1]
        # 22ms

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        sum_value = sum(nums)
        cur_value = 0
        for index,value in enumerate(nums):
            cur_value += value
            sum_value -= value
            if cur_value > sum_value:
                return nums[:index+1]   # 0ms