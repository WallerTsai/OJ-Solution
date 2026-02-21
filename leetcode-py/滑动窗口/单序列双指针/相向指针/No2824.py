from bisect import bisect_left
from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left,right = 0,len(nums)-1
        res = 0
        while left <= right:
            while left <= right and nums[left] + nums[right] < target:
                left += 1
            res += left
            right -= 1
        return res  # 少了

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        left,right =0,len(nums)-1
        while left < right:
            if nums[left] + nums[right] < target:
                res += right - left
                left += 1
            else:
                right -= 1
        return res

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        for i,num in enumerate(nums):
            res += bisect_left(nums,target-num,0,i)
        return res
