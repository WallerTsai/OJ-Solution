
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        left = right = head # 快慢指针
        while right.next != None:
            # right 走两步, left 走一步
            right = right.next
            if right.next != None:
                right = right.next
            pre = pre.next
            left = left.next
        pre.next = left.next
        return dummy.next
    

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        pre = dummy
        slow = fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        pre.next = slow.next

        return dummy.next
