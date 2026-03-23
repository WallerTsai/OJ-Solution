from itertools import pairwise
from math import inf
from typing import List


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            sub_grid = grid[i: i + k]
            for j in range(n - k + 1):
                li = []
                for row in sub_grid:
                    li.extend(row[j: j + k])
                li.sort()
                d = inf
                for x, y in pairwise(li):
                    if x < y:
                        d = min(d, y - x)
                ans[i][j] = d if d != inf else 0

        return ans

