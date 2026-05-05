from collections import defaultdict
from math import ceil

class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        li = [pow(i, 3) for i in range(1, ceil(pow(n, 1/3)))]
        cnt = defaultdict(int)
        for i in range(len(li)):
            for j in range(i + 1):
                v = li[i] + li[j]
                if v <= n:
                    cnt[v] += 1
        return sorted([k for k, v in cnt.items() if v > 1])