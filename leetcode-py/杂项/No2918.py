from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zero1 = zero2 = s1 = s2 = 0

        for num in nums1:
            if num == 0:
                zero1 += 1
                s1 += 1
            else:
                s1 += num
        
        for num in nums2:
            if num == 0:
                zero2 += 1
                s2 += 1
            else:
                s2 += num

        if s1 > s2:
            if zero2 > 0:
                return s1
        elif s2 > s1:
            if zero1 > 0:
                return s2
        else:
            return s1
        return -1   # 922ms

