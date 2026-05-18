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
        
# 2026年5月8日

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)

        mx = max(nums)
        is_prime = [True] * (mx + 1)
        is_prime[0] = is_prime[1] = False
        prime = list(range(mx + 1))
        for i in range(2, mx):
            if is_prime[i]:
                for j in range(i + i, mx + 1, i):
                    if is_prime[j]:
                        is_prime[j] = False
                        prime[j] = i

        groups = defaultdict(list)
        for i, x in enumerate(nums):
            groups[prime[x]].append(i)

        visited = set([0])
        queue =[0]
        ans = 0

        while queue:
            nx_queue = []
            for i in queue:
                if i == n - 1:
                    return ans
                
                li = groups[nums[i]]

                li.append(i + 1)
                if i:
                    li.append(i - 1)

                for j in li:
                    if j in visited:
                        continue
                    visited.add(j)
                    nx_queue.append(j)
            
            ans += 1
            queue = nx_queue

        return -1   # 错误 处理质数的时候就错了 参考 [5,2,20,1,15] 输出 4 预期 1 质因数提取不全
                

# gemini辅助：提出了 lpf 思路
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)

        mx = max(nums)
        lpf = list(range(mx + 1))
        for i in range(2, mx):
            if lpf[i] == i:
                for j in  range(i * i, mx + 1, i):
                    if lpf[j] == j:
                        lpf[j] = i

        groups = defaultdict(list)
        for i, x in enumerate(nums):
            temp = x
            while temp > 1:
                p = lpf[temp]
                groups[p].append(i)
                while temp % p == 0:
                    temp //= p

        visited = {0}
        queue = [0]
        ans = 0

        while queue:
            nx_queue = []
            for i in queue:
                if i == n - 1:
                    return ans
                
                v = nums[i]
                li = groups.pop(v, [])
                li.append(i + 1)
                if i:
                    li.append(i - 1)
                
                for j in li:
                    if j in visited:
                        continue
                    visited.add(j)
                    nx_queue.append(j)

            ans += 1
            queue = nx_queue

        return -1