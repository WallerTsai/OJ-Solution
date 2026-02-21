from typing import List 
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        res = 0
        temp,left =1,0
        for right,num in enumerate(nums):
            temp *= num
            while temp >= k:
                temp /= nums[left]
                left += 1
            res += right - left + 1     #观察得到的
        return res
