from math import inf
from typing import List


class Solution:
    # 区间取交集
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        li = []
        points.sort(key=lambda x: x[1])
        for l, r in points:
            if li and l <= li[-1][1]:
                li[-1][0] = l
            else:
                li.append([l, r])
        return len(li)  # 83ms


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        pre = -inf
        ans = 0
        for l, r in points:
            if l > pre:
                pre = r
                ans += 1
        return ans # 67ms
        