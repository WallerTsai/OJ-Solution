class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))    # 有时候是 n - 1

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def is_same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
    def merge(self, _from: int, _to: int) -> bool:
        x, y = self.find(_from), self.find(_to)
        if x == y:
            return False
        self.parent[x] = y
        return True
    
class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)  # 把size改成rank更符合"秩"的含义

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, node1: int, node2: int) -> None:
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return
        
        # 按秩合并：将秩小的树合并到秩大的树下
        if self.rank[root1] < self.rank[root2]:
            root1, root2 = root2, root1
        self.parent[root2] = root1
        if self.rank[root1] == self.rank[root2]:
            self.rank[root1] += 1

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]

    def get_size(self, x: int) -> int:
        return self.size[self.find(x)]
    
    def is_same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)