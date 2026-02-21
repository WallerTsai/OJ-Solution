from typing import List
from bisect import bisect_left
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        if len(nums1) >= len(nums2):
            used_nums = nums2
            target_nums = nums1
        else:
            used_nums = nums1
            target_nums = nums2

        for num in used_nums:
            index = bisect_left(target_nums,num)
            if index == len(target_nums):
                break
            if target_nums[index] == num:
                return num
        return -1   # 0ms

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1

        for num in nums1:
            index = bisect_left(nums2,num)
            if index == len(nums2):
                break
            if nums2[index] == num:
                return num
        return -1

class Solution:
    # 灵神一行写法
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        return min(set(nums1) & set(nums2), default=-1) # 23ms



