from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        k %= n
        for i in range(m):
            if i & 1:
                if mat[i] != mat[i][n - k:] + mat[i][:n - k]:
                    return False
            else:
                if mat[i] != mat[i][k:] + mat[i][:k]:
                    return False
        return True


