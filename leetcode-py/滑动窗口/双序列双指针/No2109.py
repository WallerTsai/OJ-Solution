from itertools import pairwise
from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        j = 0
        n = len(spaces)
        for i,c in enumerate(s):
            if j < n and i == spaces[j]:
                ans.append(" ")
                j += 1
            ans.append(c)

        return "".join(ans)

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.append(len(s))  # 这样可以在循环中处理最后一段
        ans = [s[:spaces[0]]]
        for p, q in pairwise(spaces):
            ans.append(' ')
            ans.append(s[p: q])
        return ''.join(ans)