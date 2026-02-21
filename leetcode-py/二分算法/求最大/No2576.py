from typing import List


class Solution:
    # 同向双指针
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        for x in nums[(len(nums)+1)//2:]:
            if nums[i] * 2 <= x:
                i += 1
        return i * 2 # 76ms

class Solution:
    # 二分
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        left,right = 0, len(nums)//2 + 1
        while left < right:
            mid = (left+right) // 2
            if all(nums[i] * 2 <= nums[i-mid] for i in range(mid)):
                left = mid + 1
            else:
                right = mid
        return (left - 1) * 2 # 346ms


