# 分为三步：

# 确定每种颜色的最小包围框 (Bounding Box)：
# 遍历矩阵，找到每种颜色出现的最小行/最大行、最小列/最大列。
# 这意味着该颜色当初打印时，至少涂满了这个矩形区域。

# 建立依赖图 (建边)：
# 遍历每种颜色 C 的包围框。如果在这个框内发现了其他颜色 D (C != D)，
# 说明 D 是后来覆盖上去的。这就产生了一条有向边 C -> D（代表 C 必须在 D 之前打印）。

# 拓扑排序判环：
# 使用 Kahn 算法（基于入度的 BFS）对这些颜色进行拓扑排序。
# 如果存在环（比如 A 盖住了 B，B 盖住了 C，C 又盖住了 A），
# 则说明根本无法打印，返回 false；如果能顺利排完所有颜色，返回 true。


from collections import defaultdict, deque
from typing import List


class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m, n =len(targetGrid), len(targetGrid[0])

        # borders[color] = [min_r, max_r, min_c, max_c]
        borders = dict()
        for row in range(m):
            for col in range(n):
                color = targetGrid[row][col]
                if color not in borders:
                    borders[color] = [row, row, col, col]
                else:
                    borders[color][0] = min(borders[color][0], row)
                    borders[color][1] = max(borders[color][1], row)
                    borders[color][2] = min(borders[color][2], col)
                    borders[color][3] = max(borders[color][3], col)

        g = defaultdict(set)
        indegree = defaultdict(int)
        colors = set(borders.keys())

        for color, (min_r, max_r, min_c, max_c) in borders.items():
            for r in range(min_r, max_r + 1):
                for c in range(min_c, max_c + 1):
                    cur_color = targetGrid[r][c]
                    if cur_color != color and cur_color not in g[color]:
                        g[color].add(cur_color)
                        indegree[cur_color] += 1

        q = deque([c for c in colors if indegree[c] == 0])
        count = 0
        while q:
            cur = q.popleft()
            count += 1
            for nxt in g[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return count == len(colors)

        