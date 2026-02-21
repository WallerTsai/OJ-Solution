from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
    
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        ans = 0
        visited = [False] * n
        def dfs(i):
            for j in graph[i]:
                if not visited[j]:
                    visited[j] = True
                    dfs(j)

            # 这里存在逻辑错误
            # 0 -> 1 -> 2
            # 0 -> 3
            # 在计算1时候会导致3出于未访问状态
            nonlocal ans
            ans += sum(1 for flag in visited if not flag)

        for i in range(n):
            if not visited(i):
                dfs(i)
        
        return ans
    
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # 构建图
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # 记录每个节点是否被访问过
        visited = [False] * n
        # 存储每个连通分量的大小
        component_sizes = []
        
        # DFS 函数，计算连通分量的大小
        def dfs(i):
            stack = [i]
            size = 0
            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = True
                    size += 1
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            stack.append(neighbor)
            return size
        
        # 遍历所有节点，找到每个连通分量的大小
        for i in range(n):
            if not visited[i]:
                component_size = dfs(i)
                component_sizes.append(component_size)
        
        # 计算不连通的节点对数量
        total_pairs = 0
        sum_sizes = 0
        for size in component_sizes:
            total_pairs += size * sum_sizes
            sum_sizes += size
        
        return total_pairs
    
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
    
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        ans = 0
        visited = [False] * n
        def dfs(i):
            visited[i] = True
            size = 1
            for j in graph[i]:
                if not visited[j]:
                    size += dfs(j)
            return size

        ans = temp = 0
        for i in range(n):
            if not visited[i]:
                size = dfs(i)
                ans += size * temp
                temp += size
        
        return ans 