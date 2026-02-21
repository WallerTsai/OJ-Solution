from itertools import pairwise
from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        nums.sort()
        ans = []
        
        for i, j in pairwise(range(0, len(nums) + 1, 3)):
            pattern = nums[i : j]
            if pattern[-1] - pattern[0] > k:
                return []
            ans.append(nums[i : j])

        return ans  # 104ms


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k:
                return []
            res.append(nums[i : i + 3])
        return res  # 86ms

