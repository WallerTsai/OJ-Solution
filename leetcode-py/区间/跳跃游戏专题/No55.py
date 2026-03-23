from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        for i in range(len(nums)-1):
            if i + nums[i] > mx:
                mx = i + nums[i]
        if mx >= len(nums)-1:
            return True
        return False    # 错误
    
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        for i in range(len(nums)-1):
            if i <= mx:
                mx = max(mx,i+nums[i])

        return True if mx >= len(nums)-1 else False #40ms

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        for i in range(len(nums)):
            if i > mx:
                return False
            else:
                mx = max(mx,i+nums[i])
        return True