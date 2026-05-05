from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ans =  n = len(words)
        for i, x in enumerate(words):
            if x == target:
                d = abs(i - startIndex)
                ans = min(ans, d, n - d)
        return ans if ans != n else -1


