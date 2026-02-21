# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        dummy = new_head
        head = head.next
        while head:
            if head.val == 0 and head.next:
                new_head.next = ListNode()
                new_head = new_head.next
            else:
                new_head.val += head.val
            head = head.next
        return dummy

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = h = head.next
        while dummy:
            h = h.next
            while h.val != 0:
                dummy.val += h.val
                h = h.next
            h = h.next
            dummy.next = h
            dummy = dummy.next
        return head.next    # 108ms


