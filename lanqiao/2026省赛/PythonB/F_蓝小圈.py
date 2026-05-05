import sys
sys.setrecursionlimit(100_000)
sys.set_int_max_str_digits(10_000_000)

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())

# data = sys.stdin.read().strip().split()
# it = iter(data)

out = sys.stdout.write         

class UnionFind:
    __slots__ = ["parent", "dis"]

    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.dis = [0] * (n + 1)

    def find(self, x: int) -> int:
        path = []
        root = x
        while self.parent[root] != root:
            path.append(root)
            root = self.parent[root]
        
        for node in reversed(path):
            self.dis[node] += self.dis[self.parent[node]]
            self.parent[node] = root
        return root
    

def main():
    it = map(int, sys.stdin.read().split())

    n, q = next(it), next(it)

    uf = UnionFind(n)

    personal_val = [0] * (n + 1)
    group_val = [0] * (n + 1)

    res = []
    for _ in range(q):
        op = next(it)
        if op == 1:
            x, y = next(it), next(it)
            rx, ry = uf.find(x), uf.find(y)
            if rx != ry:
                uf.parent[rx] = ry
                uf.dis[rx] = group_val[rx] - group_val[ry]
        elif op == 2:
            x, a = next(it), next(it)
            personal_val[x] += a
        elif op == 3:
            x, a = next(it), next(it)
            rx = uf.find(x)
            group_val[rx] += a
        elif op == 4:
            x = next(it)
            rx = uf.find(x)
            res.append(personal_val[x] + group_val[rx] + uf.dis[x])

    out('\n'.join(map(str, res)))
    

# 自用第四版并查集
class UnionFind:
    __slots__ = ["parent", "rank", "block_size", "block_count", "dis"]
    def __init__(self, n: int, base: int = 0):
        """
        base = 0: 节点编号 0 ~ n - 1
        base = 1: 节点编号 1 ~ n 
        """
        _size = n + 1 if base == 1 else n
        self.parent = list(range(_size))
        self.rank = [0] * _size             # 秩, 按秩合并，控制树高

        self.block_size = [1] * _size       # 每个连通块的节点数量
        self.block_count = n                # 连通块数量

        self.dis = [0] * _size              # 相对距离/权重

    def find(self, x: int) -> int:
        """ 迭代路径压缩 + 距离更新"""
        path = []
        root = x

        parent = self.parent
        dis = self.dis

        while parent[root] != root:
            path.append(root)
            root = parent[root]
        
        for node in reversed(path):
            dis[node] += dis[parent[node]]
            parent[node] = root

        return root

    def union(self, x: int, y: int) -> bool:
        """ 按秩合并 """
        return self.merge(x, y, 0)
    
    def merge(self, _from: int, _to: int, value: int = 0) -> bool:
        """ 有向合并 """
        x, y = self.find(_from), self.find(_to)
        if x == y:
            return self.dis[_from] - self.dis[_to] == value
        
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.dis[x] = value + self.dis[_to] - self.dis[_from]
            self.block_size[y] += self.block_size[x]
        else:
            self.parent[y] = x
            self.dis[y] = self.dis[_from] - self.dis[_to] - value
            self.block_size[x] += self.block_size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

        self.block_count -= 1
        return True

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
    def get_relative_dis(self, _from: int, _to: int) -> int:
        if not self.is_connected(_from, _to):
            raise ValueError(f"节点 {_from} 和 {_to} 不连通，无法计算相对距离")
        # self.find(_from)
        # self.find(_to)
        return self.dis[_from] - self.dis[_to]

    def get_block_size(self, x: int) -> int:
        """返回 x 所在连通块的节点数"""
        return self.block_size[self.find(x)]
    
    def get_block_count(self) -> int:
        """返回当前连通块总数"""
        return self.block_count


def main():
    it = map(int, sys.stdin.read().split())

    n, q = next(it), next(it)

    uf = UnionFind(n, base=1)

    personal_val = [0] * (n + 1)
    group_val = [0] * (n + 1)

    res = []
    for _ in range(q):
        op = next(it)
        if op == 1:
            x, y = next(it), next(it)
            rx, ry = uf.find(x), uf.find(y)
            if rx != ry:
                uf.merge(rx, ry, group_val[rx] - group_val[ry])
        elif op == 2:
            x, a = next(it), next(it)
            personal_val[x] += a
        elif op == 3:
            x, a = next(it), next(it)
            rx = uf.find(x)
            group_val[rx] += a
        elif op == 4:
            x = next(it)
            rx = uf.find(x)
            res.append(personal_val[x] + group_val[rx] + uf.dis[x])

    out('\n'.join(map(str, res)))



if __name__ == "__main__":
    main()