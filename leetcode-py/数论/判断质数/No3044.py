from collections import Counter
from math import isqrt
from typing import List
class Solution:

    direction = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]

    def is_Prime(self,num:int)->bool:
            if num < 2:
                return False
            for i in range(2,isqrt(num)+1):
                if num % i == 0:
                    return False
            return True

    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        cnt = Counter()
        res = -1
        for x in range(m):
            for y in range(n):
                for dx,dy in self.direction:
                    i,j = x+dx,y+dy
                    val = mat[x][y]
                    while 0 <= i < m and 0 <= j < n:
                        val = val * 10 + mat[i][j]
                        if self.is_Prime(val):
                            cnt[val] += 1
                        i += dx
                        j += dy
        
        times = 0
        for i,j in cnt.items():
            if j > times:
                res,times = i,j
            elif j == times:
                res = max(res,i)
        return res  # 72ms            
                

