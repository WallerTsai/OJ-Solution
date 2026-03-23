from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            mat = list(map(list, zip(*mat[::-1])))
        return False

class Solution:
    # No48
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

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            self.rotate(mat)
        return False