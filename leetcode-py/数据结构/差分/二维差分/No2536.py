from itertools import accumulate
from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # 二维差分
        diff = [[0] * (n + 2) for _ in range(n + 2)]
        for r1, c1, r2, c2 in queries:
            diff[r1 + 1][c1 + 1] += 1
            diff[r1 + 1][c2 + 2] -= 1
            diff[r2 + 2][c1 + 1] -= 1
            diff[r2 + 2][c2 + 2] += 1

        # 原地计算 diff 的二维前缀和，然后填入答案
        ans = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                diff[i + 1][j + 1] += diff[i + 1][j] + diff[i][j + 1] - diff[i][j]
                ans[i][j] = diff[i + 1][j + 1]
        return ans  # 195ms
    

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        table = [[0] * (n+1) for _ in range(n+1)]
        for a, b, c, d in queries:
            table[a][b] += 1
            table[c+1][d+1] += 1
            table[a][d+1] -= 1
            table[c+1][b] -= 1
        # return table
        table = [list(accumulate(table[i][:n])) for i in range(n)]
        # return table
        for i in range(1, n):
            for j in range(n):
                table[i][j] += table[i-1][j]
        return table    # 135ms
    

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]

        # 计算差分
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        mat = [[0] * n for _ in range(n)]
        for i in range(n):
            cnt = 0  # 这一行的差分和
            for j in range(n):
                cnt += diff[i][j]
                # 累加上方单元格，原地更新
                mat[i][j] = cnt if i == 0 else mat[i - 1][j] + cnt
        
        return mat  # 126ms

