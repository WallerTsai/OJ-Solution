from typing import List


class Solution:
    # No85
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        ans = 0
        for row in matrix:
            for i, x in enumerate(row):
                if x == 0:
                    heights[i] = 0
                else:
                    heights[i] += 1
            sorted_heights = sorted(heights, reverse=True)
            for j, h in enumerate(sorted_heights):
                if h == 0:
                    break
                ans = max(ans, (j + 1) * h)
        return ans



