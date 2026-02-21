from collections import deque
from typing import List


class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        graph = [[] for _ in range(n)]
        in_degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1

        queue = deque([i for i in range(n) if in_degree[i] == 0])
        position = 1
        ans = 0
        while queue:
            next_queue = deque()

            l = []
            for i in queue:
                l.append(score[i])
                for j in graph[i]:
                    in_degree[j] -= 1
                    if in_degree[j] == 0:
                        next_queue.append(j)

            for k in sorted(l):
                ans += position * k
                position += 1

            queue = next_queue

        return ans