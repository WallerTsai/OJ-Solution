from math import inf
from typing import List


class Solution:
    def get_factors(self, n:int):

        factors = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                if i != n // i:
                    factors.append(n // i)
            i += 1
        
        return factors
    def minDifference(self, n: int, k: int) -> List[int]:
        factors = self.get_factors(n)
        ans = []
        path = []
        diff = inf
        def dfs(i: int, m: int):
            if m > n:
                return 
            
            if i > k:
                return
            
            if i == k and m == n:
                nonlocal diff, ans
                MX = max(path)
                MN = min(path)
                if MX - MN < diff:
                    diff = MX - MN
                    ans = path[:]
                return
            
            for f in factors:
                path.append(f)
                dfs(i + 1, m * f)
                path.pop()

        dfs(0, 1)
        return ans  # 超时
    
class Solution:
    def get_factors(self, n:int):

        factors = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                if i != n // i:
                    factors.append(n // i)
            i += 1
        
        return sorted(factors)
    def minDifference(self, n: int, k: int) -> List[int]:
        factors = self.get_factors(n)
        ans = []
        path = []
        diff = inf
        def dfs(i: int, m: int):
            if i > k:
                return
            
            if i == k and m == 1:
                nonlocal diff, ans
                MX = max(path)
                MN = min(path)
                if MX - MN < diff:
                    diff = MX - MN
                    ans = path[:]
                return
            
            for f in factors:
                if f > m:
                    break
                if m % f:
                    continue

                path.append(f)
                dfs(i + 1, m //f)
                path.pop()

        dfs(0, n)
        return ans  # 1908ms
    
class Solution:
    # 速度靠剪枝剪出来的

    def get_factors(self, n:int):

        factors = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                if i != n // i:
                    factors.append(n // i)
            i += 1
        
        return sorted(factors)
    
    def minDifference(self, n: int, k: int) -> List[int]:
        factors = self.get_factors(n)
        ans = []
        path = []
        diff = inf

        def dfs(i: int, m: int, low: int):
            if i > k:
                return
            
            if i == k and m == 1:
                nonlocal diff, ans
                MX = max(path)
                MN = min(path)
                if MX - MN < diff:
                    diff = MX - MN
                    ans = path[:]
                return
            
            for j in range(low, len(factors)):
                f = factors[j]

                if f > m:
                    break

                if m % f:
                    continue

                path.append(f)
                dfs(i + 1, m //f, j)
                path.pop()

        dfs(0, n, 0)
        return ans  # 75ms


class Solution:
    # 速度靠剪枝剪出来的
    def minDifference(self, n: int, k: int) -> List[int]:

        factors = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                if i != n // i:
                    factors.append(n // i)
            i += 1
        factors.sort()
        
        ans = []
        path = []
        diff = inf

        def dfs(i: int, m: int, low: int):  
            if i == k - 1:

                if m < path[-1]:
                    return
                
                nonlocal diff, ans
                MX = m
                MN = path[0]
                if MX - MN < diff:
                    diff = MX - MN
                    ans = path[:] + [m]
                return
            
            for j in range(low, len(factors)):
                f = factors[j]

                if f > m:
                    break

                if m % f:
                    continue

                path.append(f)
                dfs(i + 1, m //f, j)
                path.pop()

        dfs(0, n, 0)
        return ans  # 33ms

# 灵神

# 预处理每个数的因子
MX = 100_001
divisors = [[] for _ in range(MX)]
for i in range(1, MX):
    for j in range(i, MX, i):  # 枚举 i 的倍数 j
        divisors[j].append(i)  # i 是 j 的因子

class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        min_diff = inf
        path = [0] * k
        ans = None

        def dfs(i: int, n: int, mn: int, mx: int) -> None:
            if i == k - 1:
                nonlocal min_diff, ans
                d = max(mx, n) - min(mn, n)  # 最后一个数是 n
                if d < min_diff:
                    min_diff = d
                    path[i] = n
                    ans = path.copy()  # path[:]
                return
            for d in divisors[n]:  # 枚举 x 的因子
                path[i] = d  # 直接覆盖，无需恢复现场
                dfs(i + 1, n // d, min(mn, d), max(mx, d))

        dfs(0, n, inf, 0)
        return ans  # 291ms