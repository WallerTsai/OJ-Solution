from collections import defaultdict
from typing import List


class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        n = len(conversions)
        g = defaultdict(list)
        for u, v, f in conversions:
            g[u].append((v,f))
        ans = [1] * (n + 1)
        def dfs(i:int, t:int) -> None:
            nonlocal ans
            ans[i] = t
            for v, f in g[i]:
                dfs(v,(t * f) % MOD)
        dfs(0,1)
        return ans