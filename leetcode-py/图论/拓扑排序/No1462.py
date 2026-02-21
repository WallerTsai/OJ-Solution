from collections import defaultdict, deque
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        flag = [[False] * numCourses for _ in range(numCourses)]
        g = defaultdict(list)
        indegree = [0] * numCourses

        for u, v in prerequisites:
            g[u].append(v)
            indegree[v] += 1

        q = deque(i for i,x in enumerate(indegree) if x == 0)

        while q:
            i = q.popleft()
            for j in g[i]:
                flag[i][j] = True
                for h in range(numCourses):
                    if flag[h][i]:
                        flag[h][j] = True
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

        return [flag[a][b] for a,b in queries]  # 129ms



