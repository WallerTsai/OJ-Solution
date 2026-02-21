from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 建图和记录入度
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        ans = []
        q = deque(i for i, x in enumerate(indegree) if x == 0)
        while q:
            i = q.popleft()
            ans.append(i)
            for j in graph[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
        return ans if len(ans) == numCourses else []


