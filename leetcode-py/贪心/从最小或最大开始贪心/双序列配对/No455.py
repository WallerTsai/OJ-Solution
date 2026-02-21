from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n = len(g)
        i = 0
        for j in s:
            if j >= g[i]:
                i += 1
                if i == n:
                    break
        return i
