from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        p1 = 0
        p2 = 0
        while p1 != len(nums1) and p2 != len(nums2):
            if nums1[p1][0] == nums2[p2][0]:
                res.append([nums1[p1][0],nums1[p1][1]+nums2[p2][1]])
                p1 += 1
                p2 += 1
            elif nums1[p1][0] < nums2[p2][0]:
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 += 1

        if p1 != len(nums1):
            res += nums1[p1:]

        if p2 != len(nums2):
            res += nums2[p2:]

        return res


