# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from math import inf
from typing import List, Optional


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        a = head.val
        head = head.next
        b = head.val
        head = head.next
        pos_index = 1
        pos_list = []
        MIN = inf
        while head:
            c = head.val
            if (b > a and b > c) or (b < a and b < c):
                if pos_list:
                    MIN = min(MIN,pos_index - pos_list[-1])
                pos_list.append(pos_index)
            a = b
            b = c 
            pos_index += 1
            head = head.next
        
        if len(pos_list) > 1:
            return [MIN,pos_list[-1] - pos_list[0]]
        return [-1,-1]