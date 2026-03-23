from collections import Counter
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
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        for x in cnt.values():
            if isprime[x]:
                return True
        return False



