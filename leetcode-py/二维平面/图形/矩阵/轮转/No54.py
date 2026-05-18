from typing import List


class Solution:
    def spiralOrder(self, grid: List[List[int]]) -> List[int]:
        DIR = (0, 1), (1, 0), (0, -1), (-1, 0)
        m, n = len(grid), len(grid[0])
        i = j = 0
        d = 0
        res = []
        for _ in range(m * n):
            res.append(grid[i][j])
            grid[i][j] = None
            ti, tj = i + DIR[d][0], j + DIR[d][1]
            if ti < 0 or ti >= m or tj < 0 or tj >= n or grid[ti][tj] is None:
                d = (d + 1) % 4
            i += DIR[d][0]
            j += DIR[d][1]
        return res