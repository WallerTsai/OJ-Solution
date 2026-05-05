from collections import defaultdict
from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        i1 = i2 = -1
        x1 = x2 = None
        ans = 0
        for i, x in enumerate(colors):
            if x1 is None:
                i1 = i
                x1 = x
            elif x == x1 and x2 is None:
                continue
            elif x2 is None:
                i2 = i
                x2 = x
            else:
                if x == x1:
                    ans = max(ans, i - i2)
                else:
                    ans = max(ans, i - i1)

        return max(ans, i2 - i1)


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        c = colors[0]
        if c != colors[-1]:
            return n - 1
        
        # 贪心
        r = n - 2
        while colors[r] == c:
            r -= 1

        l = 1
        while colors[l] == c:
            l += 1

        return max(r, n - 1 - l)