from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        m = n // 2
        ans = [0] * n
        for i in range(m):
            ans[i] = i + 1
            ans[i + m] = - ans[i]

        return ans



