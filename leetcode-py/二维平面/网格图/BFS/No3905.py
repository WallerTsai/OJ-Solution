from collections import deque
from heapq import heappop, heappush


class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        DIR = (1, 0), (0, 1), (-1, 0), (0, -1)
        hq = []
        visit = set()
        res = [[0] * m for _ in range(n)]
        for x, y, c in sources:
            res[x][y] = c
            heappush(hq, (0, -c, x, y))
            visit.add((x, y))

        while len(visit) < n * m:
            t, c, x, y = heappop(hq)

            for dx, dy in DIR:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and res[nx][ny] == 0:
                    res[nx][ny] = -c
                    visit.add((nx, ny))
                    heappush(hq, (t + 1, c, nx, ny))
        
        return res
        


class Solution:
    # 灵神
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        ans = [[0] * m for _ in range(n)]
        for x, y, c in sources:
            ans[x][y] = c  # 初始颜色

        sources.sort(key=lambda s: -s[2])
        q = deque(sources)

        while q:
            i, j, c = q.popleft()
            for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):  # 左右上下
                if 0 <= x < n and 0 <= y < m and ans[x][y] == 0:  # (x, y) 未着色
                    ans[x][y] = c  # 着色
                    q.append((x, y, c))  # 继续扩散

        return ans

