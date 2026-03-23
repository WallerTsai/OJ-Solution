from typing import Counter


class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        cnt = Counter(bulbs)
        return sorted(x for x, t in cnt.items() if t % 2 == 1)