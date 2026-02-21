from itertools import pairwise
from math import inf
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = inf
        ans = []
        for a, b in pairwise(arr):
            diff = b - a
            if diff < min_diff:
                min_diff = diff
                ans = [[a, b]]
            elif diff == min_diff:
                ans.append([a, b])
        return ans

