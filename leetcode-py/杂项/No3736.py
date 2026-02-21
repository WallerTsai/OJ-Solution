from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        MAX = max(nums)
        return sum(MAX - x for x in nums)


