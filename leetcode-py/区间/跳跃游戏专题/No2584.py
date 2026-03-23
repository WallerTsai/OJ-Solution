from functools import reduce
from math import gcd
import operator
from typing import List


class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        suf = reduce(operator.mul, nums)
        pre = 1
        n = len(nums)
        for i in range(n - 1):
            pre *= nums[i]
            suf //= nums[i]
            if gcd(pre, suf) == 1:
                return i
        return -1   # 超时
    

MX = 1_000_001
prime_factors = [[] for _ in range(MX)]
for i in range(2, MX):
    if not prime_factors[i]:  # i 是质数
        for j in range(i, MX, i):  # i 的倍数 j 有质因子 i
            prime_factors[j].append(i)

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        n = len(nums)
        left = dict()   # 表示质数 p 首次出现的下标
        right = [0] * n # right[i] 表示左端点为 i 的区间的右端点的最大值

        def func(p: int, i: int):
            if p in left:
                right[left[i]] = i
            else:
                left[p] = i

        for i, x in enumerate(nums):
            for j in prime_factors[x]:
                func(j, i)

        cur_right = 0
        for l, r in enumerate(right):
            if l > cur_right:
                return cur_right
            cur_right = max(cur_right, r)
        return -1