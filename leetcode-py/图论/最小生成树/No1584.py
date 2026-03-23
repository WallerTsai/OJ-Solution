from typing import List

# 自用第三版并查集
class UnionFind:
    def __init__(self, n: int, base: int = 0):
        """
        base = 0: 节点编号 0 ~ n - 1
        bsee = 1: 节点编号 1 ~ n 
        """
        _size = n + 1 if base == 1 else n
        self.parent = list(range(_size))
        self.rank = [0] * _size         # 秩, 按秩合并，控制树高
        self.block_size = [1] * _size   # 每个连通块的节点数量
        self.block_count = n                  # 连通块数量

    def find(self, x: int) -> int:
        """ 迭代路径压缩 """
        root = x
        while self.parent[root] != root:
            root = self.parent[root]

        while self.parent[x] != root:
            temp = self.parent[x]
            self.parent[x] = root
            x = temp

        return root

    def union(self, x: int, y: int) -> bool:
        """ 按秩合并 """
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.block_size[root_x] += self.block_size[root_y]
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        self.block_count -= 1

        return True
    
    def merge(self, _from: int, _to: int) -> bool:
        """ 有向合并 """
        x, y = self.find(_from), self.find(_to)
        if x == y:
            return False
        
        self.parent[x] = y
        self.block_size[y] += self.block_size[x]
        if self.rank[x] >= self.rank[y]:
            self.rank[y] = self.rank[x] + 1
        self.block_count -= 1

        return True
    
    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
    def get_block_size(self, x: int) -> int:
        """返回 x 所在连通块的节点数"""
        return self.block_size[self.find(x)]
    
    def get_block_count(self) -> int:
        """返回当前连通块总数"""
        return self.block_count
    

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                edges.append((i, j, abs(x1 - x2) + abs(y1 - y2)))
        
        edges.sort(key=lambda x: x[2])

        uf = UnionFind(n)
        ans = 0
        need = n - 1
        for u, v, w in edges:
            if uf.union(u, v):
                ans += w
                need -= 1
                if need == 0:
                    break

        return ans



