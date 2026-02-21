from collections import Counter
from functools import reduce
import math
from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cnt = Counter(deck)
        if len(set(cnt.values())) == 1 and len(cnt) != len(deck):
            return True
        return False    # 错误 [1,1,2,2,2,2]


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cnt = Counter(deck)
        li = sorted(cnt.values())
        temp = li[0]
        for t in li[1:]:
            if t % temp != 0:
                return False
        return True if temp != 1 else False # 错误 [1,1,1,1,2,2,2,2,2,2]

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cnt = Counter(deck)
        li = list(cnt.values())
        if len(li) == 1:
            return True if li[0] != 1 else False
        ans = math.gcd(li[0],li[1])
        for i in li[2:]:
            ans = math.gcd(ans,i)
        return True if ans != 1 else False
    
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return reduce(math.gcd, Counter(deck).values()) > 1