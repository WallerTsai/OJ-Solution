from collections import defaultdict
from typing import List


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        ans = 0
        def dfs(u: int, fa: int):
            res = values[u]
            for v in g[u]:
                if v != fa:
                    res += dfs(v, u)
            
            if res % k == 0:
                nonlocal ans
                ans += 1

            return res

        dfs(0, -1)
        return ans  # 107ms


class Solution:
    # 拓扑排序
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # 需要特判无边图
        if not edges:
            return 1
        
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        degree = [len(g[i]) for i in range(n)]
        st = []
        for i, d in enumerate(degree):
            if d == 1:
                st.append(i)
            values[i] %= k

        ans = 0
        while st:
            u = st.pop()
            val = values[u]
            if val == 0:
                ans += 1

            for v in g[u]:
                degree[v] -= 1
                values[v] = (values[v] + val) % k
                if degree[v] == 1:
                    st.append(v)
        
        return ans  # 225ms
