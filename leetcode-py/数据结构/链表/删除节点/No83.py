from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        pre = head
        cur = head.next
        the_set = set([pre.val])
        while cur:
            if cur.val in the_set:
                pre.next = cur.next
            else:
                the_set.add(cur.val)
                pre = cur
            cur = cur.next

        return head
