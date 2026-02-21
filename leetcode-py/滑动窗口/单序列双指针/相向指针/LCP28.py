from bisect import bisect_right
from typing import List


class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        left = 0
        right = bisect_right(nums,target-nums[left])-1

        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                ans += right-left
                left += 1
        return ans % 1_000_000_007