from itertools import pairwise
from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = pre =  left = 0
        for right, x in enumerate(prices):
            if pre - x == 1:
                ans += right - left
            else:
                left = right
            pre = x
        return ans + len(prices) # 51ms
    
    
class Solution:
    # 双指针
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = pre =  left = 0
        for right, x in enumerate(prices):
            if pre - x != 1:
                left = right
            ans += right - left + 1
            pre = x
        return ans  # 63ms


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = pre = count = 0
        for x in prices:
            if pre - x != 1:
                count = 1
            else:
                count += 1
            ans += count
            pre = x
        return ans  # 39ms
    
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        count = 1
        for a, b in pairwise(prices):
            if a - b != 1:
                count = 1
            else:
                count += 1
            ans += count
        return ans + 1  # 64ms