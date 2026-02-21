from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left,right = 1,max(nums)+1
        while left < right:
            mid = (left + right) // 2
            if sum((x-1)//mid + 1 for x in nums) <= threshold:
                right = mid
            else:
                left = mid + 1
        return left # 123ms

