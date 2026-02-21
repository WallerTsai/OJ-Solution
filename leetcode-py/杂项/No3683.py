from math import inf
from typing import List


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        ans = inf
        for s, e in tasks:
            ans = min(s + e, ans)
        return ans