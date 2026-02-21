from collections import defaultdict
from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ans = 0
        cnt = defaultdict(int)
        for word in words:
            key = tuple(sorted(set(word)))
            ans += cnt[key]
            cnt[key] += 1
        
        return ans # 15ms

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ans = 0
        cnt = defaultdict(int)
        for word in words:
            key = frozenset(word)
            ans += cnt[key]
            cnt[key] += 1
        
        return ans # 11ms
    
class Solution:
    # 灵神
    def similarPairs(self, words: List[str]) -> int:
        ans = 0
        cnt = defaultdict(int)
        for s in words:
            mask = 0
            for c in s:
                mask |= 1 << (ord(c) - ord('a'))
            ans += cnt[mask]
            cnt[mask] += 1
        return ans # 27ms