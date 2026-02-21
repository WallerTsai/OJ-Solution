from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        m = len(meetings)
        meetings.sort()
        cnt = [0] * n

        hq = []
        for i in range(min(m, n)):
            s, e = meetings[i]
            heappush(hq, (e, i))
            cnt[i] += 1

        timestamp = 0
        for i in range(n, m):
            nx_s, nx_e = meetings[i]
            while hq and hq[0][0] < nx_s:
                e, idx = heappop(hq)
                timestamp = e
                heappush(hq, (nx_s, idx))

            e, idx = heappop(hq)
            timestamp = e
            heappush(hq, (timestamp + nx_e - nx_s, idx))
            cnt[idx] += 1

        ans = temp = 0
        for i, x in enumerate(cnt):
            if x > temp:
                temp = x
                ans = i

        return ans  # 错误 不能贪心的预分配
# fun = Solution()
# fun.mostBooked(4, [[19,20],[14,15],[13,14],[11,20]])
        

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        m = len(meetings)
        meetings.sort()
        cnt = [0] * n

        hq = []
        for i in range(n):
            heappush(hq, (0, i))

        timestamp = 0
        for i in range(m):
            nx_s, nx_e = meetings[i]
            while hq and hq[0][0] < nx_s:
                e, idx = heappop(hq)
                timestamp = e
                heappush(hq, (nx_s, idx))

            e, idx = heappop(hq)
            timestamp = e
            heappush(hq, (timestamp + nx_e - nx_s, idx))
            cnt[idx] += 1

        ans = temp = 0
        for i, x in enumerate(cnt):
            if x > temp:
                temp = x
                ans = i

        return ans  # 231ms

fmin = lambda x, y: x if x < y else y
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        m = len(meetings)
        meetings.sort()
        cnt = [0] * n

        hq = [(meetings[0][0], i) for i in range(n)]
        heapify(hq)
        ans = temp = timestamp = 0
        for i in range(m):
            nx_s, nx_e = meetings[i]
            while hq and hq[0][0] < nx_s:
                e, idx = heappop(hq)
                timestamp = e
                heappush(hq, (nx_s, idx))

            e, idx = heappop(hq)
            timestamp = e
            heappush(hq, (timestamp + nx_e - nx_s, idx))
            cnt[idx] += 1
            if cnt[idx] > temp:
                temp = cnt[idx]
                ans = idx
            elif cnt[idx] == temp:
                ans = fmin(ans, idx)

        return ans  # 227ms

fun = Solution().mostBooked(2, [[0,10],[1,5],[2,7],[3,4]])


class Solution:
    # 双堆维护
    # 灵神
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        cnt = [0] * n
        idle, using = list(range(n)), list()
        meetings.sort()
        for s, e in meetings:
            # 过期的入空闲堆
            while using and using[0][0] <= s:
                heappush(idle, heappop(using)[1])
            if len(idle) == 0:  # 没有可用会议
                nx_e, i = heappop(using)
                e += nx_e - s       # ture_e = nx_e + e - s
            else:
                i = heappop(idle)
            cnt[i] += 1
            heappush(using, (e, i))

        ans = 0
        for i, x in enumerate(cnt):
            if x > cnt[ans]:
                ans = i
        
        return ans  # 203ms





