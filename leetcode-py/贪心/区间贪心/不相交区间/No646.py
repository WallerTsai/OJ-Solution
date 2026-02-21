from math import inf
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x : x[1])
        ans, right= 0, -inf
        for l, r in pairs:
            if l > right:
                ans += 1
                right = r
        return ans

