from math import inf
from typing import List


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        m, n = len(mat), len(mat[0])
        dp = {0}
        for i, row in enumerate(mat):
            nx_dp = set()
            for x in row:
                for y in dp:
                    nx_dp.add(x + y)
            dp = nx_dp

        return min(abs(x - target) for x in dp)




