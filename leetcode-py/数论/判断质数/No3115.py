from math import isqrt
from typing import List
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        
        def is_Prime(num:int)->bool:
            if num < 2:
                return False
            for i in range(2,isqrt(num)+1):
                if num % i == 0:
                    return False
            return True
        # 因为输入保证有一个素数，所以不用判断边界
        left = 0
        while not is_Prime(nums[left]):
            left += 1
        right = len(nums)-1
        while not is_Prime(nums[right]):
            right -= 1
        return right - left