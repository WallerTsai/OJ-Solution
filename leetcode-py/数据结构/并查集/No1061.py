from string import ascii_lowercase


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {ch: ch for ch in ascii_lowercase}

        def find(x: str) -> str:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def merge(x: str, y: str) -> None:
            s1, s2 = find(x), find(y)
            if s2 > s1:
                s1, s2 = s2, s1
            parent[s1] = s2

        for x, y in zip(s1, s2):
            merge(x, y)

        return "".join(find(ch) for ch in baseStr)