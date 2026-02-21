from typing import List

# 太妙了
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                if x and i and j:
                    row[j] += min(matrix[i - 1][j], matrix[i - 1][j - 1], row[j - 1])
        return sum(map(sum, matrix))