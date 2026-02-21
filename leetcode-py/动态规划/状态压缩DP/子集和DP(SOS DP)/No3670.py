from collections import defaultdict
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cnt = defaultdict(set)
        ans = 0
        for i in sorted(nums, reverse = True):
            n = i.bit_length()
            for j in range(n):
                if j & i == 0:
                    for num in cnt[j]:
                        if num & i == 0:
                            ans = max(ans,num * i)
                else:
                    cnt[j].add(i)
        return ans  # 超时
    
# 以下代码均来自灵神
# https://leetcode.cn/problems/maximum-product-of-two-integers-with-no-common-bits/solutions/3768219/mo-ban-gao-wei-qian-zhui-he-sos-dppython-78fz/

# 普通状态压缩DP
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        w = max(nums).bit_length()
        u = 1 << w
        f = [0] * u
        for x in nums:
            f[x] = x  # 初始值

        for s in range(3, u):  # 从小到大枚举集合 s（至少有两个数）
            for i in range(w):  # 枚举 s 中的元素 i
                if s >> i & 1:  # i 属于集合 s
                    v = f[s ^ (1 << i)]  # 从 s 的子集 s \ {i} 转移过来
                    if v > f[s]:
                        f[s] = v  # 手写 max 更快

        return max(x * f[(u - 1) ^ x] for x in nums)    # 19296ms
    

class Solution:
    # lowbit
    def maxProduct(self, nums: List[int]) -> int:
        w = max(nums).bit_length()
        u = 1 << w
        f = [0] * u
        for x in nums:
            f[x] = x

        for s in range(3, u):
            t = s
            while t:
                lb = t & -t
                v = f[s ^ lb]
                if v > f[s]:
                    f[s] = v
                t ^= lb

        return max(x * f[(u - 1) ^ x] for x in nums)
    

# 高维前缀和
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        w = max(nums).bit_length()
        u = 1 << w
        f = [0] * u
        for x in nums:
            f[x] = x

        for i in range(w):
            bit = 1 << i  # 避免在循环中反复计算 1 << i
            for s in range(3, u):
                if s & bit:
                    v = f[s ^ bit]
                    if v > f[s]:
                        f[s] = v

        return max(x * f[(u - 1) ^ x] for x in nums)    # 11302ms