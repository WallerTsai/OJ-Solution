from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums =set(nums)
        dummy = ListNode()
        dummy.next = head

        pre = dummy
        cur = head
        while cur:
            if cur.val in nums:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
            
        return dummy.next


