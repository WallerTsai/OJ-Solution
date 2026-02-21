from collections import defaultdict
from math import inf
from typing import List


class Solution:
    # hash map
    def minAreaRect(self, points: List[List[int]]) -> int:
        d = defaultdict(int)
        record_x = defaultdict(list)
        ans = inf

        for x, y in points:
            record_x[x].append(y)

        for x in sorted(record_x):
            col = record_x[x]
            col.sort()
            for j, y2 in enumerate(col):
                for i in range(j):
                    y1 = col[i]
                    if (y1, y2) in d:
                        ans = min(ans, (x - d[y1, y2]) * (y2 - y1))
                    d[y1, y2] = x
        
        return 0 if ans == inf else ans # 351ms


class Solution:
    # 枚举对角线
    def minAreaRect(self, points: List[List[int]]) -> int:
        s = set(map(tuple, points))
        ans = inf
        for j, p2 in enumerate(points):
            for i in range(j):
                p1 = points[i]
                if p1[0] != p2[0] and p1[1] != p2[1] and (p1[0], p2[1]) in s and (p2[0], p1[1]) in s:
                    ans = min(ans, abs((p2[0] - p1[0]) * (p2[1] - p1[1])))
        return 0 if ans == inf else ans # 931ms

