from itertools import chain
from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(sum(row) for row in grid)
        m, n = len(grid), len(grid[0])

        rows = [0] * m
        cols = [0] * n
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                rows[i] += x
                cols[j] += x

        pre = 0
        for x in rows:
            pre += x
            if pre == total - pre:
                return True
            
        pre = 0
        for x in cols:
            pre += x
            if pre == total - pre:
                return True
            
        return False


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(sum(row) for row in grid)
        def check(grid: List[List[int]]) -> bool:
            pre = 0
            for row in grid:
                pre += sum(row)
                if pre == total - pre:
                    return True
                if pre > total - pre:
                    break
            return False
        
        return check(grid) or check(list(zip(*grid)))