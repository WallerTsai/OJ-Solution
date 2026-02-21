from typing import List
from math import sqrt, inf

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def divide(n: int):
            for i in range(int(sqrt(n)),0,-1):
                if n % i == 0:
                    return (n // i, i)
                
        ans = [0,inf]
        for i in (num + 1, num + 2):
            j, k = divide(i)
            if abs(k - j) < abs(ans[1] - ans[0]):
                ans = [j, k]
        
        return ans