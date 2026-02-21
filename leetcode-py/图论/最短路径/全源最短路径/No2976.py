from collections import defaultdict
from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
    # 多次Dijkstra
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        g = defaultdict(set)
        for u, v, w in zip(original, changed, cost):
            g[ord(u) - ord('a')].add((ord(v) - ord('a'), w))

        dis = [[inf for _ in range(26)] for _ in range(26)]
        for i in range(26):
            dis[i][i] = 0
            
            hq = [(0, i)]
            while hq:
                cost, u = heappop(hq)
                if cost > dis[i][u]:
                    continue

                for v, w in g[u]:
                    new_cost = w + cost
                    if new_cost < dis[i][v]:
                        dis[i][v] = new_cost
                        heappush(hq, (new_cost, v))
            
        ans = 0
        
        for c1, c2 in zip(source, target):
            if c1 == c2:
                continue

            u = ord(c1) - ord('a')
            v = ord(c2) - ord('a')

            d = dis[u][v]

            if d == inf:
                return -1
            ans += d
        return ans  # 405ms
    

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dis = [[inf for _ in range(26)] for _ in range(26)]
        for i in range(26):
            dis[i][i] = 0

        for u, v, w in zip(original, changed, cost):
            x = ord(u) - ord('a')
            y = ord(v) - ord('a')
            if w < dis[x][y]:
                dis[x][y] = w

        for k in range(26):
            for i in range(26):
                if dis[i][k] == inf:
                    continue
                for j in range(26):
                    if dis[i][k] + dis[k][j] < dis[i][j]:
                        dis[i][j] = dis[i][k] + dis[k][j]

        ans = 0
        for c1, c2 in zip(source, target):
            if c1 == c2:
                continue

            u = ord(c1) - ord('a')
            v = ord(c2) - ord('a')

            d = dis[u][v]

            if d == inf:
                return -1
            ans += d
        return ans  # 343ms


import numpy as np # type: ignore
class Solution:
    # lc大佬 lc 最快
    def minimumCost(self, source: str, target: str, original, changed, cost) -> int:
        INF = np.int64(10**15)  # 足够大，且 INF+INF 不会溢出 int64
        d = np.full((26, 26), INF, dtype=np.int64)
        np.fill_diagonal(d, 0)

        if original:
            u = np.frombuffer(("".join(original)).encode(), dtype=np.int8) - 97
            v = np.frombuffer(("".join(changed)).encode(), dtype=np.int8) - 97
            w = np.asarray(cost, dtype=np.int64)
            np.minimum.at(d, (u, v), w)  # 重边取最小

        tmp = np.empty_like(d)
        for k in range(26):
            np.add(d[:, k:k+1], d[k:k+1, :], out=tmp)
            np.minimum(d, tmp, out=d)

        s = np.frombuffer(source.encode(), dtype=np.int8) - 97
        t = np.frombuffer(target.encode(), dtype=np.int8) - 97
        ans = d[s, t]
        return -1 if (ans >= INF).any() else int(ans.sum())
