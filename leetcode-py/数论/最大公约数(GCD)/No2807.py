# Definition for singly-linked list.

import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = pre = head
        cur = head.next
        cur: ListNode
        while cur:
            val = math.gcd(pre.val,cur.val)
            pre.next = ListNode(val=val,next=cur)
            pre = cur
            cur = cur.next
        
        return dummy    # 23ms