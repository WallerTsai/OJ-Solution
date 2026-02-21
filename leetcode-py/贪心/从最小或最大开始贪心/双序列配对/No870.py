from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums1)
        ans = [0] * m
        fix = []
        nums1.sort()
        nums2_ = []
        for i, n in enumerate(nums2):
            nums2_.append((n,i))
        nums2_.sort()
        index = 0
        for n,i in nums2_:
            while index < m and nums1[index] <= n:
                fix.append(nums1[index])
                index += 1
            if index == m :
                break
            ans[i] = nums1[index]
            index += 1
        for i, a in enumerate(ans):
            if a == 0:
                ans[i] = fix.pop()
        return ans


class Solution:
    # 灵神
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()

        n = len(nums1)
        ids = sorted(range(n), key=lambda i: nums2[i])

        ans = [0] * n
        # 左右开弓(个人理解)
        left, right = 0, n - 1
        for x in nums1:
            if x > nums2[ids[left]]:
                ans[ids[left]] = x  # 用下等马比下等马
                left += 1
            else:
                ans[ids[right]] = x  # 用下等马比上等马
                right -= 1
        return ans