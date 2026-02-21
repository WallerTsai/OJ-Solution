from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # 建图
        graph = defaultdict(list)
        indegree = {}
        for r,i in zip(recipes,ingredients):
            for s in i:
                graph[s].append(r)
            indegree[r] = len(i)
        
        # 拓扑排序
        ans = []
        q = deque(supplies)
        while q:
            for r in graph[q.popleft()]:
                indegree[r] -= 1
                if indegree[r] == 0:
                    q.append(r)
                    ans.append(r)
        
        return ans