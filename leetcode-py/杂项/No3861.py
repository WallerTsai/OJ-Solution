from math import inf


class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        t = inf
        idx = -1
        for i, x in enumerate(capacity):
            if x >= itemSize:
                if x < t:
                    t = x
                    idx = i
        return idx