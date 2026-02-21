from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        left = head

        right = head
        for _ in range(cnt):
            right = right.next

        while right:
            right = right.next
            left = left.next
        
        return left

