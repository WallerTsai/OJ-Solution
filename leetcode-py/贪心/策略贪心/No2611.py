from typing import List


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        d = sorted([y - x for x, y in zip(reward1, reward2) if y > x ], reverse=True)
        return sum(reward1) + sum(d[:n - k])    # 错误，恰好k
    

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        d = sorted([y - x for x, y in zip(reward1, reward2)], reverse=True)
        return sum(reward1) + sum(d[:n - k])    # 47ms

