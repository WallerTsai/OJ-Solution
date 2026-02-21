from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        p = q = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                continue
            p = i - 1
            break

        for i in range(p + 1, n):
            if nums[i] < nums[i - 1]:
                continue
            q = i - 1
            break

        for i in range(q + 1, len(nums)):
            if nums[i] <= nums[i - 1]:
                return False
        
        return True if p and q < n - 1 else False
    
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if nums[0] >= nums[1]:  # 一开始必须是递增的
            return False
        cnt = 1
        for i in range(2, len(nums)):
            if nums[i - 1] == nums[i]:
                return False
            if (nums[i - 2] < nums[i - 1]) != (nums[i - 1] < nums[i]):
                cnt += 1
        return cnt == 3  # 一定是增减增