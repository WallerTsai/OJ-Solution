from bisect import bisect_left
from typing import List

MX = 1_000_001
is_p = [True] * MX
is_p[0] = is_p[1] = False
prime_numbers = []
for i in range(2, MX):
    if is_p[i]:
        prime_numbers.append(i)
        for j in range(i * i, MX, i):
            is_p[j] = False

def is_prime(n: int) -> bool:
     if n < MX:
         return is_p[n]
     for p in prime_numbers:
         if p * p > n:
             break
         if n % p == 0:
             return False
     return True

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        ans = [-1,-1]
        pre = 0
        d = 100_001

        for i in range(left, right + 1):
            if is_prime(i):
                if pre and i - pre < d:
                    ans = [pre, i]
                    d = i - pre
                pre = i

        return ans  # 499ms
    
# 灵神
MX = 10 ** 6 + 1
primes = []
is_prime = [True] * MX
for i in range(2, MX):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, MX, i):
            is_prime[j] = False
primes.extend((MX, MX))  # 保证下面下标不会越界

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        p = q = -1
        i = bisect_left(primes, left)
        while primes[i + 1] <= right:
            if p < 0 or primes[i + 1] - primes[i] < q - p:
                p, q = primes[i], primes[i + 1]
            i += 1
        return [p, q]   # 55ms