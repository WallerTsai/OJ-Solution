from random import randint
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left: int, right: int):
            # 左闭右开
            i = randint(left, right - 1)
            pivot = nums[i] # 基准元素
            nums[i], nums[left] = nums[left], nums[i]

            i, j = left + 1, right - 1
            while True:
                while i <= j and nums[i] < pivot:
                    i += 1
                while i <= j and nums[j] > pivot:
                    j -= 1
                if i >= j:
                    break

                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

            nums[left], nums[j] = nums[j], nums[left]
            return j
            
        n = len(nums)
        target_idx = n - k
        left, right = 0, n
        while True:
            idx = partition(left, right)
            if idx == target_idx:
                return nums[idx]
            elif idx > target_idx:
                right = idx
            else:
                left = idx + 1


