from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        li = [(a, s) for a, s in zip(ages, scores)]
        li.sort()
        



