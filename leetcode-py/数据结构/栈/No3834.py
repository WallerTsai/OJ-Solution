
from typing import List


class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            if stack and num == stack[-1]:
                stack[-1] *= 2
                while len(stack) >= 2 and stack[-1] == stack[-2]:
                    stack.pop()
                    stack[-1] *= 2
            else:
                stack.append(num)
        return stack


class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        st = []
        for x in nums:
            st.append(x)
            while len(st) > 1 and st[-1] == st[-2]:
                st.pop()
                st[-1] *= 2
        return st

