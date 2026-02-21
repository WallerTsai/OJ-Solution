from math import inf
from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = -1
        MN = inf
        for i, (x_, y_) in enumerate(points):
            if x_ == x or y_ == y:
                d = abs(x_ - x) + abs(y_ - y)
                if MN > d:
                    ans = i
                    MN = d
        return ans