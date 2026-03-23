from collections import defaultdict
from typing import List

MX = 1_000_001
prime_factors = [[] for _ in range(MX)]
for i in range(2, MX):
    if not prime_factors[i]:  # i 是质数
        for j in range(i, MX, i):  # i 的倍数 j 有质因子 i
            prime_factors[j].append(i)

class Solution:
    # BFS
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        g = defaultdict(list)
        for i, x in enumerate(nums):
            for p in prime_factors[x]:
                g[p].append(i)

        ans = 0
        visited = set([0])
        queue = [0]

        while True:
            temp = []
            for i in queue:
                if i == n - 1:
                    return ans
                idx = g.pop(nums[i], [])
                idx.append(i + 1)
                if i: idx.append(i - 1)
                for j in idx:
                    if j in visited:
                        continue
                    visited.add(j)
                    temp.append(j)
                
            ans += 1
            queue = temp    # 923ms
        