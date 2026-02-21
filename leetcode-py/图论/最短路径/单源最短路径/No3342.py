import heapq
from math import inf
from typing import List


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
                        nt = moveTime[nx][ny] + 1 + ((nx + ny) % 2 == 0)
                    else:
                        nt = t + 1 + ((nx + ny) % 2 == 0)
                    if nt < times[nx][ny]:
                        times[nx][ny] = nt
                        heapq.heappush(hq, (nt,nx,ny))
        
        return times[-1][-1]    # 2940ms
    
class Solution:
    # leetcode 最快
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # Dijkstra，并允许同一个节点的重复访问
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # 最小堆，存储元组 (t, x, y)，表示到达 (x, y) 的时间为 t
        heap = []
        # 起点
        heapq.heappush(heap, (0, 0, 0))

        n, m = len(moveTime), len(moveTime[0])
        # time[i][j]表示到达(i,j)的最少时间
        time = [[float('inf')] * m for _ in range(n)]
        time[0][0] = 0  # 初始化

        while heap:
            t, x, y = heapq.heappop(heap)
            if t > time[x][y]:  # 剪枝
                continue
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if t < moveTime[nx][ny]:  # 需要等待
                        nt = 1 + (x + y) % 2 + moveTime[nx][ny]
                    else:  # 否则，直接进入
                        nt = t + 1 + (x + y) % 2 
                    if nt < time[nx][ny]:  # 当前的更优路径
                        time[nx][ny] = nt
                        heapq.heappush(heap, (nt, nx, ny))
                        if nx == n - 1 and ny == m - 1:
                            return nt
        return time[n - 1][m - 1]  # 终点