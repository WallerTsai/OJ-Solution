# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        stack = []
        index = 0
        while head:
            ans.append(0)
            while stack and stack[-1][1] < head.val:
                ans [stack.pop()[0]] = head.val
            stack.append([index,head.val])
            index += 1
            head = head.next
        return ans   # 27ms

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        stack = []
        n = len(nums)
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(nums[i])
        return ans # 24ms

