from collections import defaultdict, deque
from typing import List

# 题目意思是：若一个节点没有出边，则该节点是安全的；若一个节点出边相连的点都是安全的，则该节点也是安全的。
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        g = defaultdict(list)
        indegree = [0] * n
        for u, li in enumerate(graph):
            for v in li:
                g[v].append(u)
                indegree[u] += 1

        q = deque([i for i, x in enumerate(indegree) if x == 0])

        while q:
            i = q.popleft()
            for j in g[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

        return [i for i, x in enumerate(indegree) if x == 0]    # 82ms



class Solution:
    # leetcode 
    # dfs + 三色标记法
    # 0：节点尚未访问；1：节点还在某个递归栈或者环内；2：节点搜索完毕，安全
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        color = [0] * n

        def safe(x: int) -> bool:
            if color[x] > 0:
                return color[x] == 2
            color[x] = 1
            for y in graph[x]:
                if not safe(y):
                    return False
            color[x] = 2
            return True

        return [i for i in range(n) if safe(i)] # 31ms