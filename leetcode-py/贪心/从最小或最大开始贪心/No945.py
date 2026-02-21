# 难度中等
from typing import List

class Solution:
    # 贪心
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        move = 0
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                move += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1]+1
            
        return move # 151ms

class Solution:
    # 贪心
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        move = 0
        pre = -1
        for i in nums:
            if pre < i:
                pre = i
            else:
                move += pre - i +1
                pre = pre + 1
        return move # 123ms
    
    ### 一系列题目说明维护变量比数组[下标]速度更快
