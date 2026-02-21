from itertools import accumulate
from typing import List


# 灵神：
# 考虑到字母表是环形的，可以把前缀和数组延长一倍，从而变成非环形的

class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        n = 26
        next_sum = [0] * (n * 2 - 1)
        pre_sum = [0] * (n * 2 - 1)

        for i in range(n * 2 - 2):
            next_sum[i + 1] = next_sum[i] + nextCost[i % n]
            pre_sum[i + 1] = pre_sum[i] + previousCost[i % n]

        ans = 0
        a_ord = ord('a')
        for x, y in zip(s, t):
            x = ord(x) - a_ord
            y = ord(y) - a_ord
            if x == y:
                continue
            ans += min(next_sum[y + n if y < x else y] - next_sum[x],
                       pre_sum[(x + n if x < y else x) + 1] - pre_sum[y + 1])

        return ans  # 越界 pre_sum这里有个+1

# a b c     # letter
# 1 2 3     # pre_cost
# 0 1 3 6   # pre_sum


class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        n = 26
        next_sum = [0] * (n * 2)
        pre_sum = [0] * (n * 2)

        for i in range(n * 2 - 1):
            next_sum[i + 1] = next_sum[i] + nextCost[i % n]
            pre_sum[i + 1] = pre_sum[i] + previousCost[i % n]

        ans = 0
        a_ord = ord('a')
        for x, y in zip(s, t):
            x = ord(x) - a_ord
            y = ord(y) - a_ord
            if x == y:
                continue
            ans += min(next_sum[y + n if y < x else y] - next_sum[x],
                       pre_sum[(x + n if x < y else x) + 1] - pre_sum[y + 1])

        return ans