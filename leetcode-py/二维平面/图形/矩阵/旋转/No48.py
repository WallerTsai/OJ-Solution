from typing import List


class Solution:
    # (i,j)→(j,n−1−i)
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 转置
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 列翻转
        for row in matrix:
            row.reverse()


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix = list(map(list, zip(*matrix[::-1])))    # 错误 开了新的空间