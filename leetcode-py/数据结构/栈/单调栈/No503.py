from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)
        for i,n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                res[stack.pop()] = n
            stack.append(i)
        return res # 逻辑错误

class Solution:
    # 两次循环
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)
        for i,n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                res[stack.pop()] = n
            stack.append(i)
        for i,n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                res[stack.pop()] = n
        return res # 19ms

class Solution:
    # 非常巧妙
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = [i for i in range(len(nums))]

        for i,n in enumerate(nums):
            while n > nums[stack[-1]]:
                res[stack.pop()] = n
            stack.append(i)

        return res
