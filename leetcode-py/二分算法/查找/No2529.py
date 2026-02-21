from typing import List
from bisect import bisect_left,bisect_right

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        left = bisect_left(nums,0)
        right = bisect_right(nums,0)

        return max(left,len(nums)-right)
    
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(bisect_left(nums,0),len(nums)-bisect_right(nums,0))