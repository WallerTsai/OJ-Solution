from math import inf
from typing import List
# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         min_length = 0
#         right = left = 0
#         while right<len(nums):
#             if sum(nums[left:right+1]) >= target:
#                 min_length = min(right-left+1,min_length) if min_length != 0 else (right-left+1)
#                 left += 1
#                 if left > right:
#                     right += 1
#             else:
#                 right += 1
#         return min_length
#     # 非常非常慢了

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = inf    # 这样可以把循环里面的判断优化掉
        cur_sum = 0         # 这样不用重复计算总和
        left = 0
        for right,value in enumerate(nums):
            cur_sum += value
            while cur_sum >= target:
                min_length = min(right-left+1,min_length)

                cur_sum -= nums[left]
                left += 1

        return min_length if min_length <= len(nums) else 0

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)
        min_length = length+1   # 这样可以把循环里面的判断优化掉
        cur_sum = 0         # 这样不用重复计算总和
        left = 0
        for right,value in enumerate(nums):
            cur_sum += value
            while cur_sum >= target:
                min_length = min(right-left+1,min_length)

                cur_sum -= nums[left]
                left += 1

        return min_length if min_length <= length else 0

fun = Solution()
target = 7
nums = [2,3,1,2,4,3]
outcome = fun.minSubArrayLen(target,nums)
print(outcome)