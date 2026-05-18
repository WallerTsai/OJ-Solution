from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        DIR = (0, 1), (1, 0), (0, -1), (-1, 0)
        m, n = len(grid), len(grid[0])
        
        for i in range(min(m, n) // 2):
            m1, n1 = m - 2 * i, n - 2 * i
            length = 2 * (m1 + n1) - 4
            
            x = y = i
            li = []
            d = 0
            for _ in range(length):
                li.append(grid[x][y])
                x += DIR[d][0]
                y += DIR[d][1]
                if (x == i or x == i + m1 - 1) and (y == i or y == i + n1 - 1):
                    d += 1
            
            t = k % length
            li = li[t:] + li[:t]
            x = y = i
            d = 0
            for j in range(length):
                grid[x][y] =  li[j]
                x += DIR[d][0]
                y += DIR[d][1]
                if (x == i or x == i + m1 - 1) and (y == i or y == i + n1 - 1):
                    d += 1

        return grid
