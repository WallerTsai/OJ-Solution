# 预处理每个数的因子
from collections import defaultdict
from math import gcd


MX = 101
divisors = [[] for _ in range(MX)]
for i in range(1, MX):
    for j in range(i, MX, i):
        divisors[j].append(i)

class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        ans = 0
        cnt = defaultdict(int)
        for j, x in enumerate(nums):  # 枚举 j，计算左边有多少个符合要求的 i
            if j and x == nums[0]:
                ans += 1  # 单独统计 i=0 的情况
            k2 = k // gcd(k, j)  # i 必须是 k2 的倍数
            ans += cnt[(x, k2)]
            for d in divisors[j]:  # j 是 d 的倍数
                cnt[(x, d)] += 1
        return ans