# 难度简单
from heapq import nsmallest
from typing import List
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first_min_index = 1
        second_min_index = 2

        if nums[first_min_index]>nums[second_min_index]:
            first_min_index,second_min_index = second_min_index,first_min_index
        for index in range(3,len(nums)):
            if nums[index] < nums[first_min_index]:
                second_min_index = first_min_index
                first_min_index = index
            elif nums[index] < nums[second_min_index]:
                second_min_index = index
            else:
                continue

        res = nums[0] + nums[first_min_index] + nums[second_min_index]

        return res

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        s = nums[0]
        nums=nums[1:]
        nums.sort()
        return s+nums[0]+nums[1]
        

# 2026年2月1日

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        return nums[0] + sum(nsmallest(2, nums[1:]))