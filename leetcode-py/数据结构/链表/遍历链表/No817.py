# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        while head:
            if head.val in nums:
                ans += 1
                while head and head.val in nums:
                    head = head.next
            else:
                head = head.next

        return ans


