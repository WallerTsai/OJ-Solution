# 自用第四版并查集
from collections import defaultdict
from typing import List


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

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)

        for u, v in allowedSwaps:
            uf.merge(u, v)

        groups = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            groups[root].append(i)

        count = 0

        for root, indices in groups.items():
            cnt = defaultdict(int)
            temp = 0
            for idx in indices:
                cnt[source[idx]] += 1
            for idx in indices:
                cnt[target[idx]] -= 1
                if cnt[target[idx]] < 0:
                    temp += 1
            count += temp

        return n - count


class Solution:
    # 灵神
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        g = [[] for _ in range(n)]
        for i, j in allowedSwaps:
            g[i].append(j)  # 建图
            g[j].append(i)

        def dfs(x: int) -> None:
            vis[x] = True  # 避免重复访问
            # 抵消相同的元素，最终剩下 source 和 target 各自多出来的元素（对称差）
            diff[source[x]] += 1
            diff[target[x]] -= 1
            for y in g[x]:
                if not vis[y]:
                    dfs(y)

        vis = [False] * n
        ans = 0
        for x in range(n):
            if not vis[x]:
                diff = defaultdict(int)
                dfs(x)
                ans += sum(map(abs, diff.values()))
        return ans // 2  # 有 ans // 2 对多出来的元素



