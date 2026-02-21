from collections import defaultdict, deque
from typing import List

# 拓扑排序 + 动态规划
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
        n = len(colors)
        indegree = [0] * n

        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            indegree[v] += 1

        q = deque()
        dp = [[0] * 26 for _ in range(n)]
        for i, d in enumerate(indegree):
            if d == 0:
                q.append(i)
                c = ord(colors[i]) - ord('a')
                dp[i][c] += 1

        # 由拓扑结构的性质，如果存在环，则无法遍历完所有节点
        cnt = 0 # 记录遍历过节点的个数
        ans = 1
        while q:
            u = q.popleft()
            cnt += 1
            for v in g[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
                c = ord(colors[v]) - ord('a')
                for k in range(26):
                    dp[v][k] = max(dp[v][k],dp[u][k] + (c == k))
                    ans = max(ans, dp[v][k])

        return -1 if cnt < n else ans   # 1499ms
    
# 拓扑排序 + 动态规划 + 刷表法
# 注：在动态规划中，用转移来源更新当前状态叫查表法，用当前状态更新其他状态叫刷表法。
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
        n = len(colors)
        indegree = [0] * n

        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            indegree[v] += 1

        q = deque()
        dp = [[0] * 26 for _ in range(n)]
        for i, d in enumerate(indegree):
            if d == 0:
                q.append(i)
                c = ord(colors[i]) - ord('a')
                # dp[i][c] += 1

        # 由拓扑结构的性质，如果存在环，则无法遍历完所有节点
        cnt = 0 # 记录遍历过节点的个数
        ans = 1

        while q:
            u = q.popleft()
            cnt += 1

            # 更新当前状态
            c = ord(colors[u]) - ord('a')
            dp[u][c] += 1
            ans = max(ans, dp[u][c])

            # 更新其它状态
            for v in g[u]:
                for k in range(26):
                    dp[v][k] = max(dp[v][k], dp[u][k])
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        return -1 if cnt < n else ans   # 1016ms