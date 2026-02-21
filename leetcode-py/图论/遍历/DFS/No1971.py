from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()

        def dfs(i):
            if i == destination:
                return True
            visited.add(i)
            for j in graph[i]:
                if j not in visited and dfs(j):
                    return True
            return False
        
        return dfs(source)

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = [False] * n

        def dfs(i):
            if i == destination:
                return True
            visited[i] = True
            for j in graph[i]:
                if not visited[j] and dfs(j):
                    return True
            return False
        
        return dfs(source)

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = [False] * n

        def dfs(i):
            for j in graph[i]:
                if not visited[j]:
                    visited[j] = True
                    dfs(j)
        
        dfs(source)

        return visited[destination] if edges else True
