from typing import List


class Solution:
    # 脑经急转弯
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        ans = 0
        x1, y1 = startPos
        x2, y2 = homePos
        ans += sum(rowCosts[min(x1, x2) : max(x1, x2) + 1]) + sum(colCosts[min(y1, y2): max(y1, y2) + 1])
        ans -= rowCosts[x1] + colCosts[y1]
        return ans

