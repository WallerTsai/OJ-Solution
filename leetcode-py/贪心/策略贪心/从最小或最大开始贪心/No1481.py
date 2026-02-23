# 贪心5
# 难度中等

from typing import List
from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        frequent = list(Counter(arr).values())
        frequent.sort()
        while k > 0:
            if k - frequent[0] >= 0:
                k -= frequent.pop(0)
            else:
                break
        return len(frequent) # 751ms
    
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        frequent = list(Counter(arr).values())
        frequent.sort()
        res = len(frequent)
        for i in frequent:
            if k >= i:
                k -= i
                res -= 1
            else:
                break
        return res  # 39ms