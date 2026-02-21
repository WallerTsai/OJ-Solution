from math import inf
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        def min_f(target: int) -> int:
            top_sum = bottom_sum = 0
            for x, y in zip(tops, bottoms):
                if target != x and target != y:
                    return inf
                top_sum += target != x
                bottom_sum += target != y

            return min(top_sum, bottom_sum)

        ans = min(min_f(tops[0]), min_f(bottoms[0]))

        return -1 if ans == inf else ans