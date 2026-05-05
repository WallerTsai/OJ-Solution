from math import inf


class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suf_min = [inf] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf_min[i] = min(suf_min[i + 1], nums[i])

        pre_max = -inf
        for i, x in enumerate(nums):
            pre_max = max(pre_max, x)
            if pre_max - suf_min[i] <= k:
                return i
        return -1 