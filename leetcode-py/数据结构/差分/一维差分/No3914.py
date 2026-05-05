from itertools import pairwise


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        return sum(max(x - y, 0) for x, y in pairwise(nums))