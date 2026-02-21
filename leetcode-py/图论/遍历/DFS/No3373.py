from collections import defaultdict
from typing import List, Tuple

# 黑白染色
# copy by 灵神

# 对于 ans[i] 来说，新加的边的端点选取并没有本质上的区别，选自己，也就是 i 作端点即可
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:

        def count(edges: List[List[int]]) -> Tuple[dict[List[int]], List[int]]:
            g  = defaultdict(list)
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)

            cnt = [0,0] # 距离 0 节点 为 偶数， 奇数 的节点个数
            def dfs(u: int, fa: int, d: int) -> None:
                cnt[d] += 1
                for v in g[u]:
                    if v != fa:
                        dfs(v, u, d ^ 1)

            dfs(0, -1, 0)

            return g, cnt

        _, cnt2 = count(edges2)
        max2 = max(cnt2)

        g, cnt1 = count(edges1)
        ans = [max2] * len(g)
        
        def dfs(u: int, fa: int, d: int) -> None:
                ans[u] += cnt1[d]
                for v in g[u]:
                    if v != fa:
                        dfs(v, u, d ^ 1)

        dfs(0, -1, 0)
        return ans  # 698ms