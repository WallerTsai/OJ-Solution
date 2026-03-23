from heapq import heapify, heappop, heappush, heapreplace
from typing import List


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        hq = [(t, t, 1) for t in workerTimes]
        heapify(hq)
        ans = 0
        for _ in range(mountainHeight):
            cur, t, k = heappop(hq)
            ans = max(ans, cur)
            k += 1
            nxt = t * k
            heappush(hq, (nxt, t, k))
        return ans  # 错误


class Solution:
    # 灵神
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        h = [(t, t, t) for t in workerTimes]
        heapify(h)

        for _ in range(mountainHeight):
            # 工作后总用时，当前工作（山高度降低 1）用时，workerTimes[i]
            total, cur, base = h[0]
            heapreplace(h, (total + cur + base, cur + base, base))
        return total  # 最后一个出堆的 total 即为答案


