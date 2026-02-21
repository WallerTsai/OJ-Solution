from typing import List


class Solution:
    direction = (0,1),(1,0),(0,-1),(-1,0)
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        res = 0
        pos = [0,0]
        di = 0
        if [0,0] in obstacles:
            for i in range(len(commands)):
                if commands[i] > 0:
                    commands = commands[i+1:]
                    break
        for c in commands:
            if c > 0:
                x = pos[0] + self.direction[di][0]
                y = pos[1] + self.direction[di][1]
                for _ in range(c):
                    if [x,y] in obstacles:
                        break
                    x += self.direction[di][0]
                    y += self.direction[di][1]
                pos = [x-self.direction[di][0],y-self.direction[di][1]]
                res = max(res,pos[0] ** 2 + pos[1] ** 2)
            else:
                if c == -1:
                    di = (di + 1) % 4
                else:
                    di = (di - 1) % 4

        return res
    
class Solution:
    direction = (0,1),(1,0),(0,-1),(-1,0)
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        res = 0
        x = y = di = 0
        for c in commands:
            if c > 0:
                for _ in range(c):
                    nx = x + self.direction[di][0]
                    ny = y + self.direction[di][1]
                    if [nx,ny] in obstacles:
                        break
                    x,y =nx,ny
                    res = max(res,x ** 2 + y ** 2)
            else:
                if c == -1:
                    di = (di + 1) % 4
                else:
                    di = (di - 1) % 4

        return res  # 超时
    
class Solution:
    direction = (0,1),(1,0),(0,-1),(-1,0)
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        res = 0
        x = y = di = 0
        map = {(x, y) for x, y in obstacles}
        for c in commands:
            if c > 0:
                for _ in range(c):
                    nx = x + self.direction[di][0]
                    ny = y + self.direction[di][1]
                    if (nx,ny) in map:
                        break
                    x,y =nx,ny
                    res = max(res,x ** 2 + y ** 2)
            else:
                if c == -1:
                    di = (di + 1) % 4
                else:
                    di = (di - 1) % 4

        return res  # 74ms
    
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dir3 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = 0
        hs = set(map(tuple, obstacles))
        x, y = 0, 0
        ans = 0
        for j in commands:
            if j == -2:
                i = (i - 1) % 4
            elif j == -1:
                i = (i + 1) % 4
            else:
                dx, dy = dir3[i]
                for _ in range(j):
                    x2, y2 = x + dx, y + dy
                    if (x2, y2) in hs:
                        break
                    x, y = x2, y2
                ans = max(ans, x * x + y * y)
        return ans  # 39ms