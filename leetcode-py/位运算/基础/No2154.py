from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = set(nums)
        while original in nums:
            original <<= 1
        return original


class Solution:
    # 灵神
    def findFinalValue(self, nums: List[int], original: int) -> int:
        mask = 0
        for x in nums:
            if x % original == 0:
                k = x // original
                if k & (k - 1) == 0:
                    mask |= k
        mask = ~mask
        return original * (mask & -mask)
