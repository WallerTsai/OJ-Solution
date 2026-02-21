from bisect import bisect_left, bisect_right
from itertools import accumulate


MX = 500_001
is_p = [True] * MX
is_p[0] = is_p[1] = False
prime_numbers = []
for i in range(2, MX):
    if is_p[i]:
        prime_numbers.append(i)
        for j in range(i * i, MX, i):
            is_p[j] = False
pre_sum = []
for p in accumulate(prime_numbers):
    if p > MX:
        break
    if is_p[p]:
        pre_sum.append(p)
    
class Solution:
    def largestPrime(self, n: int) -> int:
        i = bisect_right(pre_sum, n)
        if i == 0 or pre_sum[i - 1] > n:
            return 0
        return pre_sum[i - 1]



