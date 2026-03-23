from bisect import bisect_left
from typing import List

MX = 1_000_001

isprime = [True] * (MX + 1)
isprime[0] = isprime[1] = False
primes = list()
# 埃拉托斯特尼筛法
for i in range(2, MX + 1):
    if isprime[i]:
        primes.append(i)
        for j in range(i + i, MX + 1, i):
            isprime[j] = False

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        pre = 0
        for x in nums:
            i = bisect_left(primes, x)
            while i > 0 and x - primes[i] <= pre:
                i -= 1
            if i > 0 and x - primes[i] > pre:
                pre = x - primes[i]
            elif x > pre:
                pre = x
            else:
                return False
        return True


# 灵神
# 设 p 是满足 x−p>pre 的最大质数，换言之，p 是小于 x−pre 的最大质数，这可以预处理质数列表后，用二分查找得到。
MX = 1000
P = [0]  # 哨兵，避免二分越界
is_prime = [True] * MX
for i in range(2, MX):
    if is_prime[i]:
        P.append(i)  # 预处理质数列表
        for j in range(i * i, MX, i):
            is_prime[j] = False

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        pre = 0
        for x in nums:
            if x <= pre: return False
            pre = x - P[bisect_left(P, x - pre) - 1]  # 减去 < x-pre 的最大质数
        return True
