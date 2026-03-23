from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            indegree[v] += 1
            indegree[u] += 1
        
        # 从外向内剥离叶子节点
        q = deque(i for i, x in enumerate(indegree) if x == 1)
        ans = [0]
        while q:
            ans.clear()
            for _ in range(len(q)):
                i = q.popleft()
                ans.append(i)
                for j in g[i]:
                    indegree[j] -= 1
                    if indegree[j] == 1:
                        q.append(j)
        
        return ans



class Solution:
    # leetcode
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        parents = [0] * n

        def bfs(start: int):
            vis = [False] * n
            vis[start] = True
            q = deque([start])
            while q:
                x = q.popleft()
                for y in g[x]:
                    if not vis[y]:
                        vis[y] = True
                        parents[y] = x
                        q.append(y)
            return x
        x = bfs(0)  # 找到与节点 0 最远的节点 x
        y = bfs(x)  # 找到与节点 x 最远的节点 y

        path = []
        parents[x] = -1
        while y != -1:
            path.append(y)
            y = parents[y]
        m = len(path)
        return [path[m // 2]] if m % 2 else [path[m // 2 - 1], path[m // 2]]