from math import inf
from collections import defaultdict
from heapq import heapify, heappop
from typing import List


class Solution:
    # dfs + 排序 + 指针
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)

        group = []  # 分组 每个连通分量一组
        node_to_group = [-1] * (c + 1) # 节点归属
        visited = [False] * (c + 1)

        def dfs(node: int, node_list: list):
            visited[node] = True
            node_list.append(node)
            for v in g[node]:
                if not visited[v]:
                    dfs(v, node_list)

        id = 0
        # 开始分组
        for i in range(1, c + 1):
            if not visited[i]:
                node_list = []
                dfs(i, node_list)
                node_list.sort()
                for node in node_list:
                    node_to_group[node] = id    # 这一步可以写进dfs
                group.append(node_list)
                id += 1

        is_online = [True] * (c + 1)
        each_group_ptr = [0] * len(group)   # 定义指针，指向所属组的当前最小值
        ans = []

        for q, x in queries:
            if q == 2:
                is_online[x] = False
                continue

            if is_online[x]:
                ans.append(x)
                continue

            group_id = node_to_group[x]

            group_list = group[group_id]
            ptr = each_group_ptr[group_id]
            
            while ptr < len(group_list) and not is_online[group_list[ptr]]:
                ptr += 1
            each_group_ptr[group_id] = ptr  # 先更新指针
            
            if ptr == len(group_list):
                ans.append(-1)
            else:
                ans.append(group_list[ptr])

            
        return ans  # 512ms



class Solution:
    # 堆 + 懒删除
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)

        id = 0  # 组id
        node_to_group = [-1] * (c + 1) # 节点归属
        group = []

        def dfs(u: int):
            node_to_group[u] = id
            hq.append(u)
            for v in g[u]:
                if node_to_group[v] == -1:
                    dfs(v)


        for i in range(1, c + 1):
            if node_to_group[i] >= 0:
                continue
            hq = []
            dfs(i)
            heapify(hq)
            group.append(hq)
            id += 1

        ans = []
        is_online = [True] * (c + 1)
        for q, x in queries:
            if q == 2:
                is_online[x] = False
                continue
            if is_online[x]:
                ans.append(x)
                continue
            hq = group[node_to_group[x]]
            while hq and not is_online[hq[0]]:
                heappop(hq)
            ans.append(hq[0] if hq else -1)
        
        return ans  # 557ms
    


class Solution:
    # 灵神
    # 倒序处理 + 维护最小值
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        g = [[] for _ in range(c + 1)]
        for x, y in connections:
            g[x].append(y)
            g[y].append(x)

        belong = [-1] * (c + 1)
        cc = 0  # 连通块编号

        def dfs(x: int) -> None:
            belong[x] = cc  # 记录节点 x 在哪个连通块
            for y in g[x]:
                if belong[y] < 0:
                    dfs(y)

        for i in range(1, c + 1):
            if belong[i] < 0:
                dfs(i)
                cc += 1

        # 记录每个节点的离线时间，初始为无穷大（始终在线）
        offline_time = [inf] * (c + 1)
        for i in range(len(queries) - 1, -1, -1):
            t, x = queries[i]
            if t == 2:
                offline_time[x] = i  # 记录离线时间

        # 每个连通块中仍在线的电站的最小编号
        mn = [inf] * cc
        for i in range(1, c + 1):
            if offline_time[i] == inf:  # 最终仍在线
                j = belong[i]
                mn[j] = min(mn[j], i)

        ans = []
        for i in range(len(queries) - 1, -1, -1):
            t, x = queries[i]
            j = belong[x]
            if t == 2:
                if offline_time[x] == i:
                    mn[j] = min(mn[j], x)  # 变回在线
            elif i < offline_time[x]:  # 已经在线（写 < 或者 <= 都可以）
                ans.append(x)
            elif mn[j] != inf:
                ans.append(mn[j])
            else:
                ans.append(-1)
        ans.reverse()
        return ans
    

# 并查集 + 最小堆
class UnionFind:

    def __init__(self, n: int):
        self.parent =  list(range(n + 1))

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def is_same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
    def merge(self, _from: int, _to: int) -> bool:
        x, y = self.find(_from), self.find(_to)
        if x == y:
            return False
        self.parent[x] = y
        return True

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:

        uf = UnionFind(c)
        for u, v in connections:
            uf.merge(u, v)

        root = [0] * (c + 1)
        for i in range(1, c + 1):
            root[i] = uf.find(i)

        comp_heap = defaultdict(list)
        for i in range(1, c + 1):
            r = root[i]
            comp_heap[r].append(i)
        for hq in comp_heap.values():
            heapify(hq)

        online = [True] * (c + 1)

        ans = []
        for q, x in queries:
            if q == 2:
                online[x] = False
                continue

            if online[x]:
                ans.append(x)
                continue

            r = root[x]
            hq = comp_heap[r]
            while hq and not online[hq[0]]:
                heappop(hq)
            ans.append(hq[0] if hq else -1)

        return ans  # 347ms




