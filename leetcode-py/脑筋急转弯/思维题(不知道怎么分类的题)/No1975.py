from math import inf
from typing import List

fmax = lambda x, y : x if x > y else y
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        biggest = -inf
        ans = count = 0
        for row in matrix:
            for x in row:
                if x < 0:
                    ans -= x
                    count += 1
                    biggest = fmax(biggest, x)

                else:
                    ans += x
        
        if count % 2:
            ans -= biggest * 2

        return ans  # 错误


fmax = lambda x, y : x if x > y else y
fmin = lambda x, y : y if x > y else x
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        abs_min = inf
        ans = count = 0
        for row in matrix:
            for x in row:
                abs_x = abs(x)
                if x < 0:
                    count += 1
                ans += abs_x
                abs_min = fmin(abs_min, abs_x)
        
        if count % 2:
            ans -= abs_min * 2

        return ans