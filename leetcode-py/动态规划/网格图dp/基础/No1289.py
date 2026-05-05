from heapq import nsmallest
from itertools import pairwise
from math import inf
from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        f = [[0] * n for _ in range(n + 1)]
        for i, row in enumerate(grid, 1):
            for j, v in enumerate(row):
                x = min((f[i - 1][k] for k in range(n) if k != j), default=0)
                f[i][j] = v + x
        return min(f[n])


class Solution:
    # 灵神
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        for pre_row, cur_row in pairwise(grid):  # 枚举上一行和当前行
            mn, mn2 = nsmallest(2, pre_row)  # 上一行的最小值和次小值
            for j, pre in enumerate(pre_row):  # 枚举上一行的状态
                cur_row[j] += mn if pre != mn else mn2  # 不是最小就加上最小，否则加上次小
        return min(grid[-1])  # 第 n-1 行的最小值


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        mn1 = mn2 = 0
        idx = -1
        for i, row in enumerate(grid):
            cur_mn1 = cur_mn2 = inf
            cur_idx = -1
            for j, x in enumerate(row):
                if j != idx:
                    x += mn1
                else:
                    x += mn2
                
                if x < cur_mn1:
                    cur_mn1, cur_mn2 = x, cur_mn1
                    cur_idx = j
                elif x < cur_mn2:
                    cur_mn2 = x
            mn1, mn2 = cur_mn1, cur_mn2
            idx = cur_idx
        return mn1