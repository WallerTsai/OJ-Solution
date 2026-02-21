# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        pre = dummy
        cur = head

        while cur:
            val = cur.val
            if cur.next and cur.next.val == val:
                cur = cur.next
                while cur.next and cur.next.val == val:
                    cur = cur.next
            else:
                pre.next = cur
                pre = cur
            cur = cur.next

        pre.next = None
        return dummy.next
