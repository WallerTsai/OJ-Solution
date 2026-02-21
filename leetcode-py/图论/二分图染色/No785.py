from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n
        for i in range(n):
            if colors[i] == -1:
                colors[i] = 0
                queue = deque([i])
                while queue:
                    u = queue.popleft()
                    for v in graph[u]:
                        if colors[v] == -1:
                            colors[v] = colors[u] ^ 1
                            queue.append(v)
                        elif colors[v] == colors[u]:
                            return False
        return True
    

class Solution:
    # 灵神
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # colors[i] = 0  表示未访问节点 i
        # colors[i] = 1  表示节点 i 为红色
        # colors[i] = -1 表示节点 i 为蓝色
        colors = [0] * len(graph)

        def dfs(x: int, c: int) -> bool:
            colors[x] = c  # 节点 x 染成颜色 c
            for y in graph[x]:
                # 邻居 y 的颜色与 x 的相同，说明不是二分图，返回 False
                # 或者继续递归，发现不是二分图，返回 False
                if colors[y] == c or \
                   colors[y] == 0 and not dfs(y, -c):  # 取相反数，实现交替染色
                    return False
            return True

        # 可能有多个连通块
        for i, c in enumerate(colors):
            if c == 0 and not dfs(i, 1):
                # 从节点 i 开始递归，发现 i 所在连通块不是二分图
                return False
        return True
    


from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.roots = list(range(n))

    def find(self, i: int) -> int:
        if self.roots[i] != i:
            self.roots[i] = self.find(self.roots[i])  # 路径压缩
        return self.roots[i]

    def is_connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    def union(self, p: int, q: int):
        self.roots[self.find(p)] = self.find(q)


class Solution:
    # 并查集
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        uf = UnionFind(n)

        for i in range(n):
            adjs = graph[i]
            if not adjs:          # 当前顶点无边，跳过
                continue
            for w in adjs:
                if uf.is_connected(i, w):   # 邻接点已与 i 同集合，冲突
                    return False
                uf.union(adjs[0], w)        # 把所有邻接点合并到同一集合
        return True # 最慢