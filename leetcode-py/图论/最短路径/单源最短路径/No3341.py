import heapq
from math import inf
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        ans = inf

        def dfs(i: int, j: int, cur_time: int):
            if i == n -1 and j == m - 1:
                nonlocal ans
                ans = min(cur_time,ans)

            if i + 1 < n:
                temp = cur_time
                if temp < moveTime[i + 1][j]:
                    temp = moveTime[i + 1][j]
                dfs(i + 1, j, temp + 1)

            if j + 1 < m:
                temp = cur_time
                if temp < moveTime[i][j + 1]:
                    temp = moveTime[i][j + 1]
                dfs(i, j + 1, temp  + 1)

        dfs(0,0,0)
        return ans  # 错误
    
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        n, m = len(moveTime), len(moveTime[0])

        hq = []
        heapq.heappush(hq,(0,0,0))
        times = [[inf] * m for _ in range(n)]
        times[0][0] = 0

        while hq:
            t, x, y = heapq.heappop(hq)
            if t > times[x][y]:
                continue
            for dx,dy in DIR:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if t < moveTime[nx][ny]:
                        nt = moveTime[nx][ny] + 1
                    else:
                        nt = t + 1
                    if nt < times[nx][ny]:
                        times[nx][ny] = nt
                        heapq.heappush(hq, (nt,nx,ny))
        
        return times[-1][-1]    # 125ms