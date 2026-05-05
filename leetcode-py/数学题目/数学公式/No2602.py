from bisect import bisect_left
from itertools import accumulate
from typing import List


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        pre_sum = list(accumulate(nums, initial=0))

        res = []
        for q in queries:
            idx = bisect_left(nums, q)
            left = idx * q - pre_sum[idx]
            right = pre_sum[n] - pre_sum[idx] - q * (n - idx)
            res.append(left + right)
        return res


