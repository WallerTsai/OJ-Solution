from collections import Counter


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        cnt = sorted(Counter(s).values())
        return sum(cnt[:-k])