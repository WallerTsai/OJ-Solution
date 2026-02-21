
import math


class Solution:
    # dfs
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        def dfs(i: int, j: int) -> bool:
            if (i,j) in vis:
                return False
            vis.add((i,j))
            if i == target or j == target or i + j == target:
                return True
            if dfs(x,j) or dfs(i,y) or dfs(0,j) or dfs(i,0):
                return True
            
            a = min(i, y - j)
            b = min(j, x - i)
            return dfs(i - a, j + a) or dfs(i + b, j - b)

        vis = set()
        return dfs(0,0)

class Solution:
# 裴蜀定理
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        return x + y >= target and target % (math.gcd(x,y)) == 0