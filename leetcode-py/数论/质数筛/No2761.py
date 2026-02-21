from math import isqrt
from typing import List


class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        if n < 2:
            return []
        res = []
        path = [1] * n
        path[0] = path[1] = [0]
        for i in range(2,isqrt(n)+1):
            if path[i] == 1:
                for x in range(i*i,n,i):
                    path[x] = 0
        for index,value in enumerate(path[:n//2+1]):
            if value == 1 and path[n-index] == 1:
                res.append([index,n-index])
        return res  # 2499
    
class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        if n < 2:
            return []
        path = [1] * n
        path[0] = path[1] = [0]
        # 预处理的时候先把质数筛选出来
        prime = []
        for i in range(2,n):
            if path[i]:
                prime.append(i)
                for x in range(i*i,n,i):
                    path[x] = 0
        
        # 如果n是奇数，那么只有奇数+偶数=奇数才符合条件，且偶数只有2符合奇数条件
        # 所有这种情况下最多只有一对满足条件
        if n % 2:
            if n > 4 and path[n-2]:
                return [[2,n-2]]
            else:
                return []
            
        res = []
        for x in prime:
            if x > n - x:
                break
            if path[n-x]:
                res.append([x,n-x])

        return res  # 3211ms
    
mx=10**6+1
path = [1] * mx
path[0] = path[1] = [0]
# 预处理的时候先把质数筛选出来
prime = []
for i in range(2,mx):
    if path[i]:
        prime.append(i)
        for x in range(i*i,mx,i):
            path[x] = 0

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        if n < 2:
            return []
        
        # 如果n是奇数，那么只有奇数+偶数=奇数才符合条件，且偶数只有2符合奇数条件
        # 所有这种情况下最多只有一对满足条件
        if n % 2:
            if n > 4 and path[n-2]:
                return [[2,n-2]]
            else:
                return []
            
        res = []
        for x in prime:
            if x > n - x:
                break
            if path[n-x]:
                res.append([x,n-x])

        return res  # 把预处理放到外面更快 47ms