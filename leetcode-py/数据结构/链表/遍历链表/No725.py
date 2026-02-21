# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        t = head
        while t:
            length += 1
            t = t.next

        div = length // k
        rem = length % k

        ans = [None for _ in range(k)]
        for i in range(min(k,length)):
            pre = None
            ans[i] = head
            for _ in range(div):
                pre = head
                head = head.next
            if rem:
                pre = head
                head = head.next
                rem -= 1
            pre.next = None

        return ans


