from bisect import bisect_left
from functools import reduce
from typing import List

class Solution:
    # 参考灵神
    def longestSubsequence(self, nums: List[int]) -> int:
        ans = 0
        w = 0
        for num in nums:
            w |= num
            
        for i in range(w):
            bit = 1 << i
            # No300
            f = []
            for x in nums:
                if x & bit == 0:
                    continue
                j = bisect_left(f, x)
                if j < len(f):
                    f[j] = x
                else:
                    f.append(x)
            ans = max(ans, len(f))
        return ans  # 超时
    

MX = 1_000_000_000
class Solution:
    # 参考灵神
    def longestSubsequence(self, nums: List[int]) -> int:
        ans = 0
        w = MX.bit_length()

        for i in range(w):
            bit = 1 << i
            # No300
            f = []
            for x in nums:
                if x & bit == 0:
                    continue
                j = bisect_left(f, x)
                if j < len(f):
                    f[j] = x
                else:
                    f.append(x)
            ans = max(ans, len(f))
        return ans


class Solution:
    # 灵神
    def longestSubsequence(self, nums: List[int]) -> int:
        ans = 0
        w = max(nums).bit_length()
        for i in range(w):
            bit = 1 << i
            # 300. 最长递增子序列
            f = []
            for x in nums:
                if x & bit == 0:  # x 二进制的第 i 位是 0
                    continue
                j = bisect_left(f, x)
                if j < len(f):
                    f[j] = x
                else:
                    f.append(x)
            ans = max(ans, len(f))
        return ans
