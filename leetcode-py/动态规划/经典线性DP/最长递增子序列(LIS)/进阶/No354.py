from bisect import bisect_left
from typing import List


class Solution:
    # 灵神
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # 双关键字排序：宽度升序，高度降序
        envelopes.sort(key=lambda e: (e[0], -e[1]))

        # 300. 最长递增子序列
        g = []
        for _, h in envelopes:
            j = bisect_left(g, h)
            if j < len(g):
                g[j] = h
            else:
                g.append(h)
        return len(g)






