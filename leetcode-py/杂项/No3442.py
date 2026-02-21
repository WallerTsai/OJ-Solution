from typing import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        max1 = max(c for c in cnt.values() if c % 2 == 1)
        min0 = min(c for c in cnt.values() if c % 2 == 0)
        return max1 - min0