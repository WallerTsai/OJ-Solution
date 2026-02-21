from typing import List
from bisect import bisect_left,bisect_right

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        for index,num in enumerate(nums):
            left = bisect_left(nums,num-k)
            right = bisect_right(nums,num+k)
            res = max(res,right-left)
            nums[index] = num + k
        return res  # 错误

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 1
        nums.sort()
        res = left = 0
        for right in range(1,len(nums)):
            if nums[right] == nums[left]:
                continue
            index = bisect_right(nums,nums[left]+2*k)
            res = max(res,index-left)
            left = right
        res = max(res,right-left+1)
        return res  # 295ms

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        res = left = 0
        left_value = nums[0] + k

        for right,num in enumerate(nums):
            while num-k > left_value:
                left += 1
                left_value = nums[left] + k
            res = max(res,right-left+1)
        
        return res  # 227ms

class Solution:
    # 最优化
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        left = 0
        left_value = nums[0] + k

        for right,num in enumerate(nums):
            if num-k > left_value:
                left += 1
                left_value = nums[left] + k
        
        return right - left + 1 # 134ms
    

