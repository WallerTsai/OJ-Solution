from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            i, cnt, sum = 1, 0, 0
            while i * i < x:
                if x % i == 0: 
                    sum += (x // i + i)
                    cnt += 2
                i += 1
                if cnt > 4: 
                    break
            if i * i == x:  # 出现这种情况 cnt 只能为奇数
                continue
            if cnt == 4:
                ans += sum
        return ans

class Solution:
    # leetcode 大佬
    def sumFourDivisors(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            upper = nums[0]
        else:
            upper = max(*nums)
        # 首先在这里筛选素数
        isPrim = [True for _ in range(upper)]
        i = 2
        while i * i < upper:
            if isPrim[i]:
                j = i * i
                while j < upper:
                    isPrim[j] = False
                    j += i
            i += 1
        # 把素数都提取出来
        prims = [i for i in range(2, upper) if isPrim[i]]
        ans = 0
        for num in nums:
            for prim in prims:
                # 已经不可能了，后续不算了
                if prim * prim > num:
                    break
                # 立方数是符合的，这个比较坑，开始没想到，比如 8
                if prim * prim * prim == num:
                    ans += (1 + num + prim + prim * prim)
                    break
                # 可以分解成两个质数乘积
                if num % prim == 0 and isPrim[num // prim] and prim * prim != num:
                    ans += (1 + num + prim + num // prim)
                    break
        return ans
    

# 2025年12月12日
from math import cbrt, isqrt
from typing import List

class Solution:
    # 暴力
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            cnt = total = 0
            sqrt_num = isqrt(num)
            if pow(sqrt_num, 2) == num:
                continue
            for i in range(1, sqrt_num + 1):
                if num % i == 0:
                    total += (num // i + i)
                    cnt += 2
                if cnt > 4:
                    break
            
            if cnt == 4:
                ans += total
        
        return ans
    

MX = 100_001
cbrt_MX = int(cbrt(MX))

isprime = [True] * (MX + 1)
primes = list()
# 埃拉托斯特尼筛法
for i in range(2, MX + 1):
    if isprime[i]:
        primes.append(i)
    for j in range(i + i, MX + 1, i):
        isprime[j] = False

# 通过质数表构造出所有的四因数
factor4 = dict()
for prime in primes:
    if prime <= cbrt_MX:
        factor4[pow(prime, 3)] = 1 + prime + pow(prime, 2) + pow(prime, 3)

for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        if primes[i] * primes[j] <= MX:
            factor4[primes[i] * primes[j]] = 1 + primes[i] + primes[j] + primes[i] * primes[j]
        else:
            break

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            if num in factor4:
                ans += factor4[num]
        return ans  # 0ms

# https://leetcode.cn/problems/four-divisors/solutions/166486/si-yin-shu-by-leetcode-solution/



# 2026年1月4日

# 预处理因子
MX = 100_001
divisor_num = [0] * MX
divisor_sum = [0] * MX
for i in range(1, MX):
    for j in range(i, MX, i):  # 枚举 i 的倍数 j
        divisor_num[j] += 1  # i 是 j 的因子
        divisor_sum[j] += i

class Solution:
    # 灵神
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            if divisor_num[x] == 4:
                ans += divisor_sum[x]
        return ans  # 4ms