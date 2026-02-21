from math import inf
from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        diff = nums[-1] - nums[0]
        for i in range(1, n):
            d = nums[i] - nums[i - 1]
            if d * diff < 0:
                return False
        return True # 特例错误
    
    
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        
        n0 = n1 = nums[0]
        for i in range(1, n):
            if nums[i] != n0:
                n1 = nums[i]
                break
        if n0 == n1:
            return True
        
        diff = n1 - n0
        for i in range(1, n):
            d = nums[i] - nums[i - 1]
            if d * diff < 0:
                return False
        
        return True
    

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase = decrease = True
        temp = nums[0]
        for num in nums:
            if num < temp:
                increase = False
            elif num > temp:
                decrease = False
            temp = num
        return increase or decrease

fun = Solution()
fun.isMonotonic([1,3,2])