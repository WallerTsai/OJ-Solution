from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        MN, MX = min(nums), max(nums)
        return (MX - MN) * k    # 19ms