from collections import defaultdict, deque
from typing import List


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # 行
        g = defaultdict(list)
        indegree = [0] * k

        for u, v in rowConditions:
            g[u - 1].append(v - 1)
            indegree[v - 1] += 1

        q = deque(i for i, x in enumerate(indegree) if x == 0)
        rows = [-1] * k
        idx = 0
        while q:
            i = q.popleft()
            rows[i] = idx
            idx += 1
            for j in g[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
        if any(x == -1 for x in rows):
            return []

        # 列
        g = defaultdict(list)
        indegree = [0] * k

        for u, v in colConditions:
            g[u - 1].append(v - 1)
            indegree[v - 1] += 1

        q = deque(i for i, x in enumerate(indegree) if x == 0)
        cols = [-1] * k
        idx = 0
        while q:
            i = q.popleft()
            cols[i] = idx
            idx += 1
            for j in g[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
        if any(x == -1 for x in cols):
            return []

        ans = [[0] * k for _ in range(k)]
        for i in range(k):
            ans[rows[i]][cols[i]] = i + 1
        return ans

