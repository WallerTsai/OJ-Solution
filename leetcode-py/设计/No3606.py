import re
from typing import List


class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        amap = {
            "electronics": 0,
            "grocery"    : 1,
            "pharmacy"   : 2,
            "restaurant" : 3
        }

        groups = [[] for _ in range(4)]
        for c, b, a in zip(code, businessLine, isActive):
            if b not in amap:
                continue
            if not a:
                continue
            if not re.fullmatch(r'[a-zA-Z0-9_]+', c):
                continue
            groups[amap[b]].append(c)
        
        ans = []
        for g in groups:
            g.sort()
            ans.extend(g)
        return ans

