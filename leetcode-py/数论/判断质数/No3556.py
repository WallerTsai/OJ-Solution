# 预处理
MX = 100_001
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
    def sumOfLargestPrimes(self, s: str) -> int:
        primes = set()
        for i in range(len(s)):
            num = 0
            for c in s[i:]:
                num = num * 10 + int(c)
                if is_prime(num):
                    primes.add(num)
        return sum(sorted(primes)[-3:]) # 71ms