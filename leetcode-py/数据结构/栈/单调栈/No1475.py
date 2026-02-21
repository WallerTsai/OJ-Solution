from typing import List
from collections import deque


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = deque()
        for i,p in enumerate(prices):
            while stack and p <= prices[stack[-1]]:
                prices[stack.pop()] -= p
            stack.append(i)
        return prices

