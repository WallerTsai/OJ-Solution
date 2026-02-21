from bisect import bisect_right
from math import inf
from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = inf
        for i, num in enumerate(nums):
            right = bisect_right(nums, num * k)
            ans = min(ans, i + n - right)
        return ans  # 267ms O( n^2 logn )
    
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = inf
        right = bisect_right(nums, nums[0] * k)
        for left, num in enumerate(nums):
            while right < n and num * k >= nums[right]:
                right += 1
            ans = min(ans, left + n - right)
        return ans  # 188ms


# 2026年2月6日
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        m = left = 0
        for right, num in enumerate(nums):
            while nums[left] * k < num:
                left += 1
            m = max(m, right - left + 1)
        return n - m