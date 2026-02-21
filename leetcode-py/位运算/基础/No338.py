from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(i.bit_count())
        return res
    
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        for i in range(n+1):
            dp[i] = i.bit_count()
        return dp