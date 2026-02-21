from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hash = [-1] * 10001
        for i,n in enumerate(nums2):
            while stack and n > nums2[stack[-1]]:
                hash[nums2[stack.pop()]] = n
            stack.append(i)
        for i,n in enumerate(nums1):
            nums1[i] = hash[n]
        return nums1
        # 也可以考虑使用字典