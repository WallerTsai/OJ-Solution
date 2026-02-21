from collections import defaultdict
from typing import List

# 哈希 + DFS
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited = [False] * len(accounts)
        # 建图
        email_to_index = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_index[email].append(i)

        def dfs(i:int) -> None:
            visited[i] = True
            for email in accounts[i][1:]:
                if email in email_set:
                    continue
                email_set.add(email)
                for j in email_to_index[email]:
                    if not visited[j]:
                        dfs(j)

        ans = []
        for i, s in enumerate(visited):
            if not s:
                email_set = set()
                dfs(i)
                ans.append([accounts[i][0]] + sorted(email_set))
        return ans

# 并查集
class UnionFind:

    def __init__(self, n: int):
        self.parent =  list(range(n))

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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_to_name = {}
        for i,account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_name:
                    uf.merge(i,email_to_name[email])
                else:
                    email_to_name[email] = i
        
        g = defaultdict(set)
        for i,account in enumerate(accounts):
            root = uf.find(i)
            g[root].update(account[1:])

        return [[accounts[root][0]] + sorted(emails) for root, emails in g.items()]

