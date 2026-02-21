from typing import List

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
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)

        for eq in equations:
            if eq[1] == "=":
                uf.merge(ord(eq[0])-ord('a'), ord(eq[3])-ord('a'))

        for eq in equations:
            if eq[1] == "!":
                if uf.is_same(ord(eq[0])-ord('a'), ord(eq[3])-ord('a')):
                    return False
        
        return True