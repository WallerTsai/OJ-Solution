from bisect import bisect_left
from collections import defaultdict
from math import inf
from typing import List


class Solution:
    # cv by 灵神
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        # 记录每种字母出现的位置
        pos = defaultdict(list)
        for i, c in enumerate(s):
            pos[c].append(i)

        # 构建有向图
        g = defaultdict(list)
        for i, p in pos.items():
            l, r = p[0], p[-1]
            for j, q in pos.items():
                if j == i:
                    continue
                k = bisect_left(q,l)
                if k < len(q) and q[k] <= r:
                    g[i].append(j)
                    # 相交的全部连起来
        
        def dfs(x: str) -> None:
            nonlocal l, r
            visited.add(x)
            p = pos[x]
            # 合并区间
            l = min(l,p[0])
            r = max(r,p[-1])
            for v in g[x]:
                if v not in visited:
                    dfs(v)

        intervals = []
        for i, p in pos.items():
            visited = set()
            l, r = inf, 0
            dfs(i)
            intervals.append((l,r))

        # 参考 No.435
        # 统计无重叠区间
        ans = []
        intervals.sort(key=lambda x: x[1])
        pre_right = -1
        for l, r in intervals:
            if l > pre_right:
                ans.append(s[l:r + 1])
                pre_right = r
        
        return ans