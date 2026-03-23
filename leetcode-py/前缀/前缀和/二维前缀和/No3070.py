from math import inf
from typing import List


class Solution:
    # 二维前缀和
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                pre_sum[i + 1][j + 1] = pre_sum[i][j + 1] + pre_sum[i + 1][j] - pre_sum[i][j] + x
                if pre_sum[i + 1][j + 1] <= k:
                    ans += 1
        return ans


