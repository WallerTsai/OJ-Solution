from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        ans = 0

        row_sum = [sum(row) for row in mat]
        col_sum = [sum(col) for col in zip(*mat)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                    ans += 1
                    break
        return ans