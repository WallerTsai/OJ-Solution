from bisect import bisect_left
from math import inf
from typing import List


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        index = -1
        diff = 0
        length = len(nums1)
        for i in range(length):
            d = abs(nums1[i] - nums2[i])
            if d > diff:
                index = i
                diff = d
            res += d
        if index != -1:
            nums1.sort()
            find = nums2[index]
            replace_index = bisect_left(nums1,find)
            if replace_index == length:
                new_diff = find - nums1[replace_index-1]
            elif replace_index == 0:
                new_diff = nums1[0] - find
            else:
                new_diff = min(nums1[replace_index] - find,find - nums1[replace_index-1])
            res = res - diff + new_diff
        return res # 错误 # 相差最大的那个，可能不发生改变

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        index = -1
        fixed = 0
        length = len(nums1)
        sorted_nums1 = sorted(nums1)
        for i in range(length):
            # 需要每一次都遍历
            diff = abs(nums1[i]-nums2[i])
            res += diff
            index = bisect_left(sorted_nums1,nums2[i])
            if index: # index > 0
                fixed = min(fixed,nums2[i] - sorted_nums1[index-1] - diff)
            if index < length:
                fixed = min(fixed,sorted_nums1[index] - nums2[i] - diff)
        return (res + fixed) % 1_000_000_007 if res else 0 # 251ms

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        res = fixed = 0
        index = -1
        length = len(nums1)
        sorted_nums1 = sorted(nums1)
        for i in range(length):
            diff = abs(nums1[i]-nums2[i])
            res += diff
            if diff < -fixed:
                continue    # 剪枝 
            index = bisect_left(sorted_nums1,nums2[i])
            if index: # index > 0
                fixed = min(fixed,nums2[i] - sorted_nums1[index-1] - diff)
            if index < length:
                fixed = min(fixed,sorted_nums1[index] - nums2[i] - diff)
        return (res + fixed) % 1_000_000_007 if res else 0  # 59ms

fun = Solution()
out = fun.minAbsoluteSumDiff([1,28,21],[9,21,20])