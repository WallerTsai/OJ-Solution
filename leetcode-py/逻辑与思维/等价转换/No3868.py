from collections import defaultdict, Counter
from typing import List


class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:

        nums1.sort()
        nums2.sort()
        if nums1 == nums2:
            return 0
        
        n = len(nums1)
        i = j = 0
        cnt1 = cnt2 = 0
        while i < n and j < n:
            if nums1[i] == nums2[j]:
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                if j + 1 < n and nums2[j + 1] == nums2[j]:
                    j += 2
                    cnt1 += 1
                else:
                    return -1
            else:
                if i + 1 < n and nums1[i + 1] == nums1[i]:
                    i += 2
                    cnt2 += 1
                else:
                    return -1
                
        while i < n:
            if i + 1 < n and nums1[i + 1] == nums1[i]:
                i += 2
                cnt2 += 1
            else:
                return -1
            
        while j < n:
            if j + 1 < n and nums2[j + 1] == nums2[j]:
                j += 2
                cnt1 += 1
            else:
                return -1
            
        return cnt1 // 2 if cnt2 == cnt1 else -1
                


class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:

        nums1.sort()
        nums2.sort()
        if nums1 == nums2:
            return 0
        
        n = len(nums1)
        i = j = 0
        cnt1 = cnt2 = 0
        while i < n and j < n:
            if nums1[i] == nums2[j]:
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                if j + 1 < n and nums2[j + 1] == nums2[j]:
                    j += 2
                    cnt1 += 1
                else:
                    return -1
            else:
                if i + 1 < n and nums1[i + 1] == nums1[i]:
                    i += 2
                    cnt2 += 1
                else:
                    return -1
                
        while i < n:
            if i + 1 < n and nums1[i + 1] == nums1[i]:
                i += 2
                cnt2 += 1
            else:
                return -1
            
        while j < n:
            if j + 1 < n and nums2[j + 1] == nums2[j]:
                j += 2
                cnt1 += 1
            else:
                return -1
            
        return cnt1 if cnt2 == cnt1 else -1
    



class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        cnt = defaultdict(int)
        cnt1 = defaultdict(int)
        for num in nums1:
            cnt[num] += 1
            cnt1[num] += 1
        for num in nums2:
            cnt[num] += 1
        for v in cnt.values():
            if v % 2 == 1:
                return -1
        ans = 0
        for k, v in cnt.items():
            ans += abs(v // 2 - cnt1[k])
        return ans // 2
            

# 由于两个集合的大小都是 n，根据 diff 的定义，diff 的总和（出现次数之差的总和）是 n−n=0。
# 换句话说，diff 中的正数之和等于负数之和的绝对值。集合 A 多出的数，恰好也是集合 B 多出的数。

class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        ans = 0
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        for k in set(nums1 + nums2):
            if (c1[k] + c2[k]) % 2 == 1:
                return -1
            x1 = c1[k]
            x2 = c2[k]
            ans += abs(x1 - x2) // 2
            
        return ans // 2
    

class Solution:
    def minCost(self, nums1: List[int], nums2: List[int]) -> int:
        diff = Counter(nums1)
        diff.subtract(nums2)

        ans = 0
        for d in diff.values():
            if d % 2:
                return -1
            if d > 0:
                ans += d
        return ans // 2