from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x**2 for x in nums])
    

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0] * length
        left = 0
        right = length -1 
        for i in range(length-1,-1,-1):
            if nums[left] ** 2 > nums[right] ** 2:
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1
        return res  # 15ms
            
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0] * length
        left = 0
        right = length -1 
        for i in range(length-1,-1,-1):
            x,y = nums[left],nums[right]
            if x < 0 and -x > y:
                res[i] = x ** 2
                left += 1
            else:
                res[i] = y ** 2
                right -= 1
        return res
