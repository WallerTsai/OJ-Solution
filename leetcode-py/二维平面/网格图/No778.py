from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        hq = [(grid[0][0], 0, 0)]
        l =  0
        visited = {(0, 0)}
        DIR = (1, 0), (0, 1), (-1, 0), (0, -1)
        while hq:
            cur_l, x, y = heappop(hq)
            l = max(l, cur_l)
            if x == y == n - 1:
                return l
            for dx, dy in DIR:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    heappush(hq, (grid[nx][ny], nx, ny))
                    visited.add((nx, ny))



class Solution:
    # 灵神
    # 二分
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # 判断在只访问 grid[i][j] <= mx 的情况下，能否到达终点
        def check(mx: int) -> bool:
            vis = set()

            def dfs(i: int, j: int) -> bool:
                if i == j == n - 1:  # 到达终点
                    return True
                vis.add((i, j))  # 标记访问过，避免重复访问
                for x, y in (i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1):  # 按照这个顺序访问邻居，代码跑得快（和数据有关系）
                    if 0 <= x < n and 0 <= y < n and grid[x][y] <= mx and (x, y) not in vis and dfs(x, y):
                        return True
                return False

            return dfs(0, 0)

        left = max(grid[0][0], grid[-1][-1])
        right = n * n - 1
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return right
    

class Solution:
    # 灵神
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dis = [[inf] * n for _ in range(n)]
        dis[0][0] = grid[0][0]
        h = [(grid[0][0], 0, 0)]  # 堆中保存 (起点到 (i,j) 的最少时间, i, j)

        while True:
            d, i, j = heappop(h)
            if i == j == n - 1:  # 到终点的最短路已确定
                return d
            if d > dis[i][j]:  # (i,j) 之前出堆过
                continue
            for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):  # 顺序无所谓，我们只看堆中最小的
                if 0 <= x < n and 0 <= y < n:
                    new_dis = max(d, grid[x][y])
                    if new_dis < dis[x][y]:
                        dis[x][y] = new_dis  # 更新 (i,j) 的邻居的最短路
                        # 懒更新堆：只插入数据，不更新堆中数据
                        # 相同节点可能有多个不同的 new_dis，除了最小的 new_dis，其余值都会触发上面的 continue
                        heappush(h, (new_dis, x, y))