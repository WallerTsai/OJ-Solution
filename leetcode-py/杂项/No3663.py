from collections import defaultdict
from math import inf


class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        cnt = defaultdict(int)
        while n:
            temp = n % 10
            cnt[temp] += 1
            n //= 10

        a = b = inf
        for i, t in cnt.items():
            if t < b:
                a = i
                b = t
            elif t == b:
                a = min(a, i)
        
        return a