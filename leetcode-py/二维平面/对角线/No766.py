from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n, m = len(matrix), len(matrix[0])
        # 令 k = i - j + m 右上角 k = 1, 左下角 k = m + n - 1
        # i = k + j - m
        for k in range(1, m + n):
            min_j = max(m - k,0)
            max_j = min(m + n - 1 - k, m - 1)
            a = [matrix[k + j - m][j] for j in range(min_j, max_j + 1)]
            if len(set(a)) != 1:
                return False
            
        return True

class Solution:
    # by 负雪明烛
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix) - 1):
            if matrix[i][:-1] != matrix[i + 1][1:]:
                return False
        return True

