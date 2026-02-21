from math import factorial
from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 1_000_000_007
        s = complexity[0]
        if any (x <= s for x in complexity[1:]):
            return 0
        return factorial(len(complexity) - 1) % MOD # 263ms
    

from functools import reduce
MOD = 1_000_000_007
factorial_reduce = lambda n: reduce(lambda x, y: x*y%MOD, range(1, n+1), 1)
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        s = complexity[0]
        if any (x <= s for x in complexity[1:]):
            return 0
        return factorial_reduce(len(complexity) - 1)    # 19ms
    

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 1_000_000_007
        ans = 1
        for i in range(1, len(complexity)):
            if complexity[i] <= complexity[0]:
                return 0
            ans = ans * i % MOD
        return ans  # 31ms