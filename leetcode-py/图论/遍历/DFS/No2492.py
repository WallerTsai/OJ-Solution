from math import inf
from collections import defaultdict
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        for u,v,d in roads:
            g[u-1].append((v-1,d))
            g[v-1].append((u-1,d))

        ans = inf
        visited = [False] * n

        def dfs(i:int):
            nonlocal ans
            visited[i] = True
            for v,d in g[i]:
                ans = min(ans,d)
                if not visited[v]:
                    dfs(v)
        
        dfs(0)
        return ans
    
