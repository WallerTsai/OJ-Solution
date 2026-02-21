from typing import List


class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        ans = []
        pow10 = 1
        while n:
            n, d = divmod(n, 10)
            if d:
                ans.append(d * pow10)
            pow10 *= 10
        ans.reverse()
        return ans