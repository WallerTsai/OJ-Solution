from typing import List

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
    def splitArray(self, nums: List[int]) -> int:
        prime_sum = not_prime_sum = 0
        for i, num in enumerate(nums):
            if is_prime(i):
                prime_sum += num
            else:
                not_prime_sum += num
        return abs(prime_sum - not_prime_sum)   # 83ms