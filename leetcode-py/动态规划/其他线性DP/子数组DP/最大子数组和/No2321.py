from math import inf
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf
        f = 0
        for x in nums:
            f = max(f, 0) + x
            ans = max(ans, f)
        return ans
    
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        li1 = []
        li2 = []
        for a, b in zip(nums1, nums2):
            li1.append(a - b)
            li2.append(b - a)

        s1 = self.maxSubArray(li1)
        s2 = self.maxSubArray(li2)

        return max(sum(nums1) + s2, sum(nums2) + s1)


# ans1 = s1 - (nums1[left] + ... + nums1[right]) + (nums2[left] + ... + nums2[right])
# 令：diff[i] = nums2[i] - nums1[i]
# ans1 = s1 + (diff[left] + ... + diff[right])
# argmax ans1 == argmax (diff[left] + ... + diff[right])
# ans2 同理