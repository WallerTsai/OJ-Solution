from typing import List


class Solution:
    # 三指针
    def sortColors(self, nums: List[int]) -> None:
        i, left, right = 0, -1, len(nums)
        while i < right:
            if nums[i] == 0:
                left += 1
                nums[left], nums[i] = nums[i], nums[left]
                i += 1
            elif nums[i] == 2:
                right -= 1
                nums[i], nums[right] = nums[right], nums[i]
            else:
                i += 1
        
class Solution:
    # 灵神
    def sortColors(self, nums: List[int]) -> None:
        p0 = p1 = 0
        for i, x in enumerate(nums):
            nums[i] = 2
            if x <= 1:
                nums[p1] = 1
                p1 += 1
            if x == 0:
                nums[p0] = 0
                p0 += 1