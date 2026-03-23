from math import inf
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
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        must_uf = UnionFind(n)
        all_uf = UnionFind(n)
        min_s = inf
        max_s = 0
        for x, y, s, must in edges:
            if must and not must_uf.merge(x, y):
                return -1   # 成环
            all_uf.merge(x, y)
            min_s = min(min_s, s)
            max_s = max(max_s, s)

        if all_uf.get_block_count() > 1:
            return -1   # 图不连通
        
        def check(low: int) -> bool:
            u = UnionFind(n)
            for x, y, s, must in edges:
                if must and s < low:
                    return False
                if must or s >= low:
                    u.merge(x, y)

            left_k = k
            for x, y, s, must in edges:
                if left_k == 0 or u.get_block_count() == 1:
                    break
                if not must and s < low <= s * 2 and u.merge(x, y):
                    left_k -= 1
            
            return u.get_block_count() == 1
        
        left, right = min_s, max_s * 2 + 1
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid

        return left - 1 # 1820ms
    


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
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        uf = UnionFind(n)
        all_uf = UnionFind(n)
        min_s1 = inf
        for x, y, s, must in edges:
            if must:
                if not uf.merge(x, y):  # 必选边成环
                    return -1
                min_s1 = min(min_s1, s)
            all_uf.merge(x, y)

        if all_uf.get_block_count() > 1:  # 图不连通
            return -1
        
        if uf.get_block_count() == 1:
            return min_s1
        

        # Kruskal 求最大生成树
        edges.sort(key=lambda e: -e[2])
        a = []
        for x, y, s, must in edges:
            if not must and uf.merge(x, y):
                a.append(s)

        # 答案为如下三者的最小值：
        # 1. must = 1 中的最小边权
        # 2. a 中最小边权 * 2
        # 3. a 中第 k+1 小边权
        ans = min(min_s1, a[-1] * 2)
        if k < len(a):
            ans = min(ans, a[-1 - k])
        return ans  # 404ms

