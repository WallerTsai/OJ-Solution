from collections import defaultdict
from typing import Dict, List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        
        def bulit_adj(edges: List[List[int]]) -> Dict[List[int]]:
            # 构建邻接表
            # n = len(edges + 1)
            g = defaultdict(list)
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)

            return g
        
        def dfs(g: List[List[int]], u: int, fa: int, d: int) -> int:
            if d < 0:
                return 0
            cnt = 1
            for v in g[u]:
                if v != fa:
                    cnt += dfs(g, v, u, d - 1)
            return cnt
        
        n, m = len(edges1) + 1, len(edges2) + 1
        g2 = bulit_adj(edges=edges2)
        max2 = max(dfs(g2, i, -1, k - 1) for i in range(m))
        
        g1 = bulit_adj(edges=edges1)

        return [dfs(g1, i, -1, k) + max2 for i in range(n)] # 1863ms