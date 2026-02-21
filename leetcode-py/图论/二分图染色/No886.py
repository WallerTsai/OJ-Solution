from collections import defaultdict, deque
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = defaultdict(list)
        for u, v in dislikes:
            g[u].append(v)
            g[v].append(u)

        colors = [-1] * (n + 1)
        for i in range(n):
            if colors[i] == -1:
                colors[i] = 0
                q = deque([i])
                while q:
                    u = q.popleft()
                    for v in g[u]:
                        if colors[v] == -1:
                            colors[v] = colors[u] ^ 1
                            q.append(v)
                        elif colors[v] == colors[u]:
                            return False
        return True





