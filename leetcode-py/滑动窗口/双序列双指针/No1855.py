from typing import List


class Solution:
    # 朴素写法
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        for i,num in enumerate(nums1):
            for j in range(i,len(nums2)):
                if num > nums2[j]:
                    break
                res = max(res,j-i)
        return res  # 超时

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        pre_index = 0
        pre_num = nums1[0]
        for i,num in enumerate(nums1):

            if num > pre_num:
                continue

            for j in range(pre_index,len(nums2)):
                if num > nums2[j]:
                    pre_index = j
                    pre_num = nums2[j]
                    break

                res = max(res,j-i)

            if pre_index == len(nums2)-1:
                break

        return res  # 407ms

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        pre_index = 0
        pre_num = nums1[0]
        for i,num in enumerate(nums1):

            if num > pre_num:
                pre_index += 1
                continue

            while pre_index < len(nums2):
                if num > nums2[pre_index]:
                    pre_num = nums2[pre_index]
                    break
                res = max(res,pre_index-i)
                pre_index += 1

            if pre_index == len(nums2)-1:
                break

        return res  # 163ms
    
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        pre_index = 0
        pre_num = nums1[0]
        for i,num in enumerate(nums1):
            if pre_index == len(nums2)-1:
                break

            if num > pre_num:
                pre_index += 1
                continue

            while pre_index < len(nums2):
                if num > nums2[pre_index]:
                    pre_num = nums2[pre_index]
                    break
                pre_index += 1
            res = max(res,pre_index-i-1)

        return res # 83ms
    
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        length_1 = len(nums1)
        length_2 = len(nums2)
        pre_index_1 = pre_index_2 = 0
        # 只大不小
        while pre_index_1 < length_1 and pre_index_2 < length_2:
            if nums1[pre_index_1] > nums2[pre_index_2]:
                pre_index_1 += 1
            pre_index_2 += 1
        return max(pre_index_2 - pre_index_1 -1,0)  # 19ms

# 不难发现 指针2必增加 指针1特定条件才增加


