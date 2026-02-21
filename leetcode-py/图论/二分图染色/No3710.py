from collections import defaultdict, deque
from typing import List


class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 2:
            return 0
        
        dist = []
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dist.append((d, i, j))

        dist.sort()

        def check(mid: int):
            g = defaultdict(list)
            for d, i, j in dist:
                if d < mid:
                    g[i].append(j)
                    g[j].append(i)
                else:
                    break

            # 二分图染色
            colors = [-1] * n
            for i in range(n):
                if colors[i] == -1:
                    colors[i] = 0
                    queue = deque([i])
                    while queue:
                        u = queue.popleft()
                        for v in g[u]:
                            if colors[v] == -1:
                                colors[v] = colors[u] ^ 1
                                queue.append(v)
                            elif colors[v] == colors[u]:
                                return False
            return True

            
        left, right = 0, dist[-1][0] + 1
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid
        return left - 1