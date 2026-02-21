from collections import Counter
from typing import List


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        ans = 0
        n1,n2 = len(nums1),len(nums2)

        for num in nums2:
            target = num ** 2
            l,r = 0,n1-1
            while l < r:
                if nums1[l] * nums1[r] > target:
                    r -= 1
                elif nums1[l] * nums1[r] < target:
                    l += 1
                else:
                    ans += 1
                    l += 1
                    r -= 1

        for num in nums1:
            target = num ** 2
            l,r = 0,n2-1
            while l < r:
                if nums2[l] * nums2[r] > target:
                    r -= 1
                elif nums2[l] * nums2[r] < target:
                    l += 1
                else:
                    ans += 1
                    l += 1
                    r -= 1
        return ans  # 错误
    
class Solution:
    def numTriplets(self,nums1:List[int],nums2:List[int]) -> int:
        n1,n2 = len(nums1),len(nums2)
        ans = 0
        cnt1 = Counter([num ** 2 for num in nums1])
        cnt2 = Counter([num ** 2 for num in nums2])

        for i in range(n2):
            for j in range(i+1,n2):
                if nums2[i] * nums2[j] in cnt1:
                    ans += cnt1[nums2[i] * nums2[j]]

        for i in range(n1):
            for j in range(i+1,n1):
                if nums1[i] * nums1[j] in cnt2:
                    ans += cnt2[nums1[i] * nums1[j]] 
        
        return ans # 231ms

class Solution:
    # leetcode 大佬
    # hash-map + 双指针
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        c1, c2 = Counter(nums1), Counter(nums2)
        key1 = sorted(c1.keys())
        key2 = sorted(c2.keys())

        for num in key1:
            target = num * num
            left, right = 0, len(key2) - 1
            while left <= right:
                if key2[left] * key2[right] > target:
                    right -= 1
                elif key2[left] * key2[right] < target:
                    left += 1
                else:
                    if left == right:
                        ans += c1[num] * (c2[key2[left]] * (c2[key2[right]] - 1) // 2)
                    else:
                        ans += c1[num] * c2[key2[left]] * c2[key2[right]]
                    right -= 1

        for num in key2:
            target = num * num
            left, right = 0, len(key1) - 1
            while left <= right:
                if key1[left] * key1[right] > target:
                    right -= 1
                elif key1[left] * key1[right] < target:
                    left += 1
                else:
                    if left == right:
                        ans += c2[num] * (c1[key1[left]] * (c1[key1[right]] - 1) // 2)
                    else:
                        ans += c2[num] * c1[key1[left]] * c1[key1[right]]
                    right -= 1
    
        return ans