from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)

        left, right = 0, n - 1
        sum_left = nums[0]
        sum_right = nums[-1]
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                sum_left += nums[i]
                left = i
            else:
                break

        for j in range(n - 2, -1, -1):
            if nums[j] > nums[j + 1]:
                sum_right += nums[j]
                right = j
            else:
                break

        
        if left == right:
            return min(abs(sum_left - sum_right + nums[right]), abs(sum_left - nums[left] - sum_right))

        elif left + 1 == right:
            return abs(sum_left - sum_right)
        
        else:
            return -1