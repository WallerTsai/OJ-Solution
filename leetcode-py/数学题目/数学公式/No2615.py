from collections import defaultdict
from typing import List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)

        groups = defaultdict(list)
        for i, num in enumerate(nums):
            groups[num].append(i)

        res = [0] * n
        for group in groups.values():
            total = sum(group)
            pre_sum = 0
            m = len(group)
            for i, idx in enumerate(group):
                res[idx] = total - 2 * pre_sum + idx * (2 * i - m)
                pre_sum += idx

        return res





