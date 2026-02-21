from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = left = pre_num = 0
        for right,num in enumerate(nums):
            k -= (num-pre_num) * (right - left)
            while k < 0:
                k += num - nums[left]
                left += 1
            res = max(res,right-left+1)
            pre_num = num
        return res  # 267ms

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = pre_num = 0
        for right,num in enumerate(nums):
            k -= (num-pre_num) * (right - left)
            if k < 0:
                k += num - nums[left]
                left += 1
            pre_num = num
        return right-left+1 # 175ms
