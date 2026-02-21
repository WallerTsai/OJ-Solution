from collections import Counter
from typing import List


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.cnt1 = Counter(nums1)
        self.nums2 = nums2
        self.cnt2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        num = self.nums2[index]
        self.nums2[index] += val
        self.cnt2[num] -= 1
        self.cnt2[num + val] += 1

    def count(self, tot: int) -> int:
        ans = 0
        for key, value in self.cnt1.items():
            ans += value * self.cnt2[tot - key]

        return ans
