from collections import defaultdict
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        g = defaultdict(list)
        for i,x in enumerate(graph):
            g[i].extend(x)

        res = []
        def dfs(i:int,path:list):
            path.append(i)
            if i == n-1:
                res.append(path[:])
            for x in g[i]:
                dfs(x,path[:])
        
        dfs(0,[])
        return res

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        path = [0]

        def dfs(x:int,n:int):
            if x == n:
                res.append(path[:])
                return
            
            for i in graph[x]:
                path.append(i)
                dfs(i,n)
                path.pop()
            
        dfs(0,n-1)
        return res