from collections import defaultdict
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        cnt = [len(g[i]) for i in range(n)]
        visited = set()
        def dfs(i:int):
            visited.add(i)
            path.append(i)
            for v in g[i]:
                if v not in visited:
                    dfs(v)

        ans =  0
        for i in range(n):
            path = []
            if i not in visited:
                dfs(i)
                ans += 1
            for u in path:
                if cnt[u] != len(path) - 1:
                    ans -= 1
                    break
            path.clear()
        return ans  # 64ms
    
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        vis = [False] * n
        def dfs(x: int) -> None:
            vis[x] = True
            nonlocal v, e
            v += 1
            e += len(g[x])
            for y in g[x]:
                if not vis[y]:
                    dfs(y)

        ans = 0
        for i, b in enumerate(vis):
            if not b:
                v = e = 0
                dfs(i)
                ans += e == v * (v - 1)
        return ans