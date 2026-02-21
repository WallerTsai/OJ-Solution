from collections import defaultdict
from typing import List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        answer = 0
        d = defaultdict(int)
        for i in rectangles:
            d[i[0]/i[1]] += 1
        for i in d:
            n = d[i]
            answer += n*(n-1)/2
        return int(answer)

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ans = 0
        ratio = [x / y for x, y in rectangles]
        cnt = Counter(ratio)
        for v in cnt.values():
            ans += v * (v - 1) // 2
        return ans

