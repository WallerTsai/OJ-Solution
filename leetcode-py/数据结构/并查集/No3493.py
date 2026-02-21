from collections import defaultdict
from typing import List


class Solution:
    # DFS
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        set_list = [set(p) for p in properties]
        n = len(set_list)
        g = defaultdict(list)

        for i in range(n-1):
            for j in range(i+1, n):
                if len(set_list[i] & set_list[j]) >= k:
                    g[i].append(j)
                    g[j].append(i)

        visited = set()

        def dfs(i: int) -> None:
            visited.add(i)
            for v in g[i]:
                if v not in visited:
                    dfs(v)
        
        ans = 0
        for i in range(n):
            if i not in visited:
                ans += 1
                dfs(i)
        
        return ans
    

class UnionFind:
    def __init__(self,n: int):
        self.parent = list(range(n))
        self.cc = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def is_same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(x)
    
    def merge(self, _from: int, _to: int) -> bool:
        x, y = self.find(_from), self.find(_to)
        if x == y:
            return False
        self.parent[x] = y
        self.cc -= 1
        return True

class Solution:
    # 并查集
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        sets = list(map(set, properties))
        uf = UnionFind(len(sets))
        for i, a in enumerate(sets):
            for j, b in enumerate(sets[:i]):
                if len(a & b) >= k:
                    uf.merge(j,i)
        return uf.cc


