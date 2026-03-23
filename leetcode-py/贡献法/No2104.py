from typing import List


class Solution:
    # 单调栈 + 贡献法
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        min_stack, max_stack = [], []

        min_left = [-1] * n
        max_left = [-1] * n
        min_right = [n] * n
        max_right = [n] * n

        for i, num in enumerate(nums):
            while min_stack and nums[min_stack[-1]] > num:
                min_right[min_stack[-1]] = i
                min_stack.pop()
            if min_stack:
                min_left[i] = min_stack[-1]
            min_stack.append(i)

            while max_stack and nums[max_stack[-1]] <= num:
                max_right[max_stack[-1]] = i
                max_stack.pop()
            if max_stack:
                max_left[i] = max_stack[-1]
            max_stack.append(i)

        ans = 0
        for i, (x, max_r ,max_l, min_r, min_l) in enumerate(zip(nums, max_right, max_left, min_right, min_left)):
            ans += x * ((max_r - i) * (i - max_l) - (min_r - i) * (i - min_l))
            
        return ans




