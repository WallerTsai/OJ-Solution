from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        ans = 0
        for i in range(n):
            pre = -1
            for j in range(m):
                if grid[j][i] > pre:
                    pre = grid[j][i]
                else:
                    pre += 1
                    ans += pre - grid[j][i]
        return ans

