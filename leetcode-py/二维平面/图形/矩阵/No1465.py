from itertools import pairwise
from typing import List

MOD = 1_000_000_007
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        max_h = max_w = 0

        pre = 0
        horizontalCuts.append(h)
        horizontalCuts.sort()
        for x in horizontalCuts:
            max_h = max(max_h, x - pre)
            pre = x

        pre = 0
        verticalCuts.append(w)
        verticalCuts.sort()
        for x in verticalCuts:
            max_w = max(max_w, x - pre)
            pre = x

        return (max_h * max_w) % MOD


class Solution:
    # 灵神
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]
        max_h = max(q - p for p, q in pairwise(horizontalCuts))
        max_w = max(q - p for p, q in pairwise(verticalCuts))
        return max_h * max_w % (10 ** 9 + 7)