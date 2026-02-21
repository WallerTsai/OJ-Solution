from functools import cache
from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        @cache
        def dfs(i:int) -> int:
            if i >= n:
                return 0
            p, next = questions[i]
            return max(p + dfs(i + next + 1),dfs(i + 1))
        return dfs(0)

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        f = [0] * (n + 1)
        for i in range(n - 1,-1,-1):
            j = min(i + questions[i][i] + 1, n)
            f[i] = max(f[i + 1], f[j] + questions[i][0])
        return f[0]