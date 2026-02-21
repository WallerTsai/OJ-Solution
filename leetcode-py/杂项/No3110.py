from itertools import pairwise


class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for x,y in pairwise(map(ord,s)):
            ans += abs(x-y)
        return ans