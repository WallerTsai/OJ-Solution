from bisect import bisect_left
from math import inf
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        li = []
        for x in nums:
            i = bisect_left(li, x)
            if i == 2:
                return True
            if i == len(li):
                li.append(x)
            else:
                li[i] = x
        return False
    
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = b = inf
        for x in nums:
            if x <= a:
                a = x
            elif x <= b:
                b = x
            else:
                return True
        return False