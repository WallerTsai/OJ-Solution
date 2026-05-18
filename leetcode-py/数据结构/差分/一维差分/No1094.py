from collections import Counter
from itertools import accumulate
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        mx = max(x[2] for x in trips) + 1
        d = [0] * mx
        for num, f, t in trips:
            d[f] += num
            d[t] -= num

        return all(s <= capacity for s in accumulate(d))



class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cnt = Counter()
        for i,from_,to in trips:
            cnt[from_] += i
            cnt[to] -= i
        cur = 0
        for num in sorted(cnt):
            cur += cnt[num]
            if cur > capacity:
                return False
        return True