# 难度中等
from typing import List
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        for i,happy in enumerate(happiness):
            if i >= k : 
                break
            if happy - i <= 0:
                break
            else:
                res += happy - i

        return res  # 118ms
    
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        for i,happy in enumerate(happiness[:k]):
            if happy <= i:
                break
            res += happy - i
        return res  # 111ms