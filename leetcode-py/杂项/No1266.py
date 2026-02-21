from itertools import pairwise
from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for p1, p2 in pairwise(points):
            x1, y1 = p1
            x2, y2 = p2
            ans += max(abs(x1 - x2), abs(y1 - y2))
        return ans



