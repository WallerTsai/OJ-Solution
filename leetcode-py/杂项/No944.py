from itertools import pairwise
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for l in zip(*strs):
            for a, b in pairwise(l):
                if b < a:
                    ans += 1
                    break
        return ans  # 55ms


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for col in zip(*strs):
            if any(x > y for x, y in pairwise(col)):
                ans += 1
        return ans  # 71ms
