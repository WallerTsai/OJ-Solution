from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        n = 1
        tail = head
        while tail.next:
            n += 1
            tail = tail.next

        k %= n

        m = n - k - 1
        cur = head
        while m:
            cur = cur.next
            m -= 1
        
        tail.next = head
        head = cur.next
        cur.next = None

        return head



