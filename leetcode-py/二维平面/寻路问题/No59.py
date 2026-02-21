from typing import List


class Solution:
    direction = [(0,1),(1,0),(0,-1),(-1,0)]
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for _ in range(n)]
        y = x = di = 0

        for val in range(1,n**2+1):
            ans[y][x] = val

            next_y = y + self.direction[di][0]
            next_x = x + self.direction[di][1]
            if (not (0 <= next_x < n)) or (not (0 <= next_y < n)) or ans[next_y][next_x]:
                di = (di+1) % 4
            y += self.direction[di][0]
            x += self.direction[di][1]

        return ans