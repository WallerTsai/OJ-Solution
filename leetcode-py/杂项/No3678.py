from math import ceil
from typing import List


class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        n = len(nums)
        avg = sum(nums) // n
        for i in range(max(avg + 1, 1),200):
            if i not in nums:
                return i
            
class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        n = len(nums)
        avg = sum(nums) // n
        ans = max(1, avg + 1)
        nums_set = set(nums)
        while ans in nums_set:
            ans += 1
        return ans