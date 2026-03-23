from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        pre_sum = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]

        ans = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                pre_sum[i + 1][j + 1][0] = pre_sum[i + 1][j][0] + pre_sum[i][j + 1][0] - pre_sum[i][j][0]
                pre_sum[i + 1][j + 1][1] = pre_sum[i + 1][j][1] + pre_sum[i][j + 1][1] - pre_sum[i][j][1]
                if x == 'X':
                    pre_sum[i + 1][j + 1][0] += 1
                elif x == 'Y':
                    pre_sum[i + 1][j + 1][1] += 1
                if pre_sum[i + 1][j + 1][0] > 0 and pre_sum[i + 1][j + 1][0] == pre_sum[i + 1][j + 1][1]:
                    ans += 1
        return ans


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        col_x = [0] * n
        col_y = [0] * n
        ans = 0
        for i, row in enumerate(grid):
            pre_x = pre_y = 0
            for j, x in enumerate(row):
                if x == 'X':
                    col_x[j] += 1
                elif x == 'Y':
                    col_y[j] += 1
                pre_x += col_x[j]
                pre_y += col_y[j]
                if pre_x == pre_y and pre_x > 0:
                    ans += 1
        return ans  # 269ms