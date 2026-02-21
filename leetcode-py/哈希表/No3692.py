from collections import defaultdict
from typing import Counter


class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        cnt = Counter(s)
        n = max(cnt.values())
        l = []
        for k, v in cnt.items():
            if v == n:
                l.append(k)
        return ''.join(l)
    
class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        cnt = Counter(s)
        cnt2 = Counter(cnt.values())

        f = n = 0
        for k, v in cnt2.items():
            if v > n:
                n = v
                f = k
            elif v == n:
                if k > f:
                    n = v
                    f = k

        l = []
        for k, v in cnt.items():
            if v == f:
                l.append(k)
        return ''.join(l)


class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        cnt = Counter(s)
        groups = defaultdict(list)
        k = 0
        
        for ch, f in cnt.items():
            groups[f].append(ch)
            if (len(groups[f]), f) > (len(groups[k]), k):
                k = f

        return ''.join(groups[k])


