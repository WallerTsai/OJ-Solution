from functools import reduce
from math import gcd, lcm
from typing import List

# 参考 No.238
# copy by 灵神
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        suf_gcd = [0] * (n + 1)
        suf_lcm = [0] * n + [1]
        for i in range(n - 1, -1, -1):
            suf_gcd[i] = gcd(suf_gcd[i + 1], nums[i])
            suf_lcm[i] = lcm(suf_lcm[i + 1], nums[i])

        ans = suf_gcd[0] * suf_lcm[0]  # 不移除元素
        pre_gcd, pre_lcm = 0, 1
        for i, x in enumerate(nums):  # 枚举移除 nums[i]
            ans = max(ans, gcd(pre_gcd, suf_gcd[i + 1]) * lcm(pre_lcm, suf_lcm[i + 1]))
            pre_gcd = gcd(pre_gcd, x)
            pre_lcm = lcm(pre_lcm, x)
        return ans  # 4ms
    
class Solution:
    # 暴力
    def maxScore(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0] ** 2
        ans = reduce(lcm, nums) * reduce(gcd, nums)
        for x in set(nums):
            nums1 = list(nums)
            nums1.remove(x)
            ans = max(ans, reduce(lcm, nums1) * reduce(gcd, nums1))
        return ans  # 23ms