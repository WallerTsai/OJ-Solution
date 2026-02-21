from bisect import bisect_left
from itertools import accumulate
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        accumulater = accumulate(nums,initial=0)
        self.nums = list(accumulater)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right+1] - self.nums[left]


