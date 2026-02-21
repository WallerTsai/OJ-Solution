from heapq import heappush
from itertools import pairwise
from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        hq = []
        for l, r in pairwise(nums):
            heappush((r - l,l,r))

        # 不应该这样写， 反例差值[4, 3, 1, 2, 5] 2 如果选了1，就选不了[3，2]了


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        diff_list = [r - l for l, r in pairwise(nums)]

        def check(MAX: int) -> bool:
            count = 0
            i = 0
            while i < n - 1:
                if diff_list[i] <= MAX:
                    i += 1
                    count += 1
                i += 1
            return count >= p
        
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left # 291ms

