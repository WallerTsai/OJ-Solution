from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        groups = defaultdict(list)
        for a, b, t in meetings:
            groups[t].append([a, b])
        
        aset = set([0, firstPerson])
        for t in sorted(groups.keys()):
            g = defaultdict(list)
            temp_set = set()
            for a, b in groups[t]:
                g[a].append(b)
                g[b].append(a)
                if a in aset:
                    temp_set.add(a)
                if b in aset:
                    temp_set.add(b)
            
            # bfs
            q = deque(list(temp_set))
            while q:
                a = q.popleft()
                for b in g[a]:
                    if b not in aset:
                        aset.add(b)
                        q.append(b)

        return list(aset)   # 418ms
    

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        known = set([0, firstPerson])

        n = len(meetings)
        i = 0
        while i < n:
            g = defaultdict(list)
            cur_t = meetings[i][2]
            while i < n and meetings[i][2] == cur_t:
                a, b, _ = meetings[i]
                g[a].append(b)
                g[b].append(a)
                i += 1

            visited = set()

            def dfs(x: int):
                visited.add(x)
                known.add(x)
                for y in g[x]:
                    if y not in visited:
                        dfs(y)

            for a in g:
                if a in known and a not in visited:
                    dfs(a)

        return list(known)  # 363ms


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
    
class Solution:
    # 灵神
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # 按照 time 从小到大排序
        meetings.sort(key=lambda x: x[2])

        uf = UnionFind(n)
        # 一开始 0 和 firstPerson 都知道秘密
        uf.merge(firstPerson, 0)

        # 分组循环
        m = len(meetings)
        i = 0
        while i < m:
            start = i
            time = meetings[i][2]
            # 合并在同一时间发生的会议
            while i < m and meetings[i][2] == time:
                x, y, _ = meetings[i]
                uf.merge(x, y)
                i += 1

            # 如果节点不和 0 在同一个集合，那么撤销合并，恢复成初始值
            for x, y, _ in meetings[start: i]:
                if not uf.is_same(x, 0):
                    uf.parent[x] = x
                if not uf.is_same(y, 0):
                    uf.parent[y] = y

        # 和 0 在同一个集合的专家都知道秘密
        return [i for i in range(n) if uf.is_same(i, 0)]
        # 取消合并那一步没有想到

