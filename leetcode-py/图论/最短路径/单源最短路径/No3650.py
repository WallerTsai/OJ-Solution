from collections import defaultdict
import heapq
from math import inf
from typing import List


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        reversed_adj = defaultdict(list)
        
        for u, v, w in edges:
            adj[u].append((v, w))
            reversed_adj[v].append((u, w))

        heap = []
        heapq.heappush(heap, (0, 0, False))

        dist = {}
        dist[(0, False)] = 0

        ans = inf
        while heap:
            cur_cost, u, used = heapq.heappop(heap)

            if u == n - 1:
                ans = min(ans, cur_cost)
                continue
            if cur_cost > dist.get((u, used), inf):
                continue

            for v, w in adj[u]:
                new_cost = cur_cost + w
                if (v, used) not in dist or new_cost < dist[(v, used)]:
                    dist[(v, used)] = new_cost
                    heapq.heappush(heap, (new_cost, v, used))

            if not used:
                for v, w in reversed_adj[u]:
                    new_cost = cur_cost + w * 2
                    if (v, True) not in dist or new_cost < dist[(v, True)]:
                        dist[(v, True)] = new_cost
                        heapq.heappush(heap, (new_cost, v, True))

        return ans if ans != inf else -1
    
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        reversed_adj = defaultdict(list)
        
        for u, v, w in edges:
            adj[u].append((v, w))
            reversed_adj[v].append((u, w))

        heap = []
        heapq.heappush(heap, (0, 0))

        dist = {}
        dist[(0, False)] = 0

        ans = inf
        while heap:
            cur_cost, u = heapq.heappop(heap)

            if u == n - 1:
                ans = min(ans, cur_cost)
                continue
            if cur_cost > dist.get(u, inf):
                continue

            for v, w in adj[u]:
                new_cost = cur_cost + w
                if v not in dist or new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(heap, (new_cost, v))

            for v, w in reversed_adj[u]:
                new_cost = cur_cost + w * 2
                if v not in dist or new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(heap, (new_cost, v))

        return ans if ans != inf else -1
    
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, 2 * w))

        heap = []
        heapq.heappush(heap, (0, 0))

        dist = {}
        dist[0] = 0

        while heap:
            cur_cost, u = heapq.heappop(heap)

            if u == n - 1:
                return cur_cost
            if cur_cost > dist.get(u, inf):
                continue

            for v, w in adj[u]:
                new_cost = cur_cost + w
                if v not in dist or new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(heap, (new_cost, v))

        return -1
    
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]  # 邻接表
        for x, y, wt in edges:
            g[x].append((y, wt))
            g[y].append((x, wt * 2))

        dis = [inf] * n
        dis[0] = 0  # 起点到自己的距离是 0
        h = [(0, 0)]  # 堆中保存 (起点到节点 x 的最短路长度，节点 x)

        while h:
            dis_x, x = heapq.heappop(h)
            if dis_x > dis[x]:  # x 之前出堆过
                continue
            if x == n - 1:  # 到达终点
                return dis_x
            for y, wt in g[x]:
                new_dis_y = dis_x + wt
                if new_dis_y < dis[y]:
                    dis[y] = new_dis_y  # 更新 x 的邻居的最短路
                    # 懒更新堆：只插入数据，不更新堆中数据
                    # 相同节点可能有多个不同的 new_dis_y，除了最小的 new_dis_y，其余值都会触发上面的 continue
                    heapq.heappush(h, (new_dis_y, y))

        return -1


# 2026年1月27日
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for u, v, w, in edges:
            g[u].append((v, w))
            g[v].append((u, w * 2))

        dis = [inf] * n
        dis[0] = 0
        hq = [(0, 0)]

        while hq:
            d, u = heapq.heappop(hq)
            if d > dis[u]:
                continue
            if u == n - 1:
                return d
            for v, w in g[u]:
                new_dis = d + w
                if new_dis < dis[v]:
                    dis[v] = new_dis
                    heapq.heappush(hq, (new_dis, v))
        
        return -1

        



