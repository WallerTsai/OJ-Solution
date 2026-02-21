from itertools import accumulate
from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1

        for num, d in zip(nums,accumulate(diff)):
            if num > d:
                return False
        return True # 63ms

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        
        n = len(nums)
        diff = [nums[i] - nums[i - 1] for i in range(1,n)]
        diff = [nums[0]] + diff + [0]

        for l, r in queries:
            diff[l] -= 1
            diff[r + 1] += 1
        
        for num in accumulate(diff[:-1]):
            if num > 0:
                return False
        return True # 137ms
