from itertools import pairwise
from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = target[0]
        for a, b in pairwise(target):
            if b > a:
                ans += b - a

        return ans

