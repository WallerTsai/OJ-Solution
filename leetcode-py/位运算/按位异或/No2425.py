from typing import List


print(1 ^ 3)
print(1 ^ 2)
print(2 ^ 3)
print(1 ^ 1 ^ 3 ^ 2)

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1) % 2
        n2 = len(nums2) % 2
        ans = 0
        if n1:
            for num in nums2:
                ans ^= num
        if n2:
            for num in nums1:
                ans ^= num
        return ans  # 7ms
