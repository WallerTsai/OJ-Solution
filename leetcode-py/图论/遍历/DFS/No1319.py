from collections import defaultdict
from typing import List

# 进行dfs统计图的个数和线的总数
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)
        visited = [False] * n

        line_count = graph_count = 0
        def dfs(i):
            visited[i] = True
            count = 0
            for j in graph[i]:
                count += 1
                if not visited[j]:
                    count += dfs(j)
            return count

        for i in range(n):
            if not visited[i]:
                graph_count += 1
                line_count += dfs(i)

        line_count /= 2


        if line_count >= n - 1:
            return graph_count - 1
        else:
            return -1   # 45ms

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)
        visited = [False] * n

        line_count = graph_count = 0
        def dfs(i):
            for j in graph[i]:
                if not visited[j]:
                    visited[j] = True
                    dfs(j)

        for i in range(n):
            if not visited[i]:
                graph_count += 1
                dfs(i)

        line_count = len(connections)
        

        if line_count >= n - 1:
            return graph_count - 1
        else:
            return -1   # 52ms

fun = Solution()
print(fun.makeConnected(4,[[0,1],[0,2],[1,2]]))