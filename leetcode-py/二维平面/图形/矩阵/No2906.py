from functools import reduce
from operator import mul
from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        rows = []
        for row in grid:
            rows.append(reduce(mul, row))
        total = reduce(mul, rows)

        ans = []
        for i, row in enumerate(grid):
            part = total // rows[i]
            li = []
            for j, x in enumerate(row):
                temp = rows[i] // x
                li.append((temp * part) % MOD)
            ans.append(li)
        return ans

    # (A / B) % MOD != (A % MOD) / (B % MOD)


class Solution:
    # 前后缀分解 + 取模优化
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        MOD = 12345

        ans = [[0] * n for _ in range(m)]

        pre = 1
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                ans[i][j] = pre
                pre = (pre * x) % MOD

        suf = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                ans[i][j] = (ans[i][j] * suf) % MOD
                x = grid[i][j]
                suf = (suf * x) % MOD
        
        return ans