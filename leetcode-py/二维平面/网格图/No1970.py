from collections import deque
from typing import List

DIRS = (0, 1), (0, -1), (1, 0), (-1, 0)
class Solution:
    # 二分 + bfs
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def check(t: int):
            g = [[0] * col for _ in range(row)]
            for i in range(t):
                r, c = cells[i]
                g[r - 1][c - 1] = 1

            q = deque()
            for i, x in enumerate(g[0]):
                if x == 0:
                    q.append((0, i))
                    g[0][i] = 1 # 标记已经访问

            while q:
                r, c = q.popleft()
                if r == row - 1:
                    return True
                
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and g[nr][nc] == 0:
                        q.append((nr, nc))
                        g[nr][nc] = 1

            return False
        
        left = 1
        right = len(cells)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid

        return left - 1 # 937ms
    

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def is_same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
    def merge(self, _from: int, _to: int) -> bool:
        x, y = self.find(_from), self.find(_to)
        if x == y:
            return False
        self.parent[x] = y
        return True

DIRS = (0, 1), (0, -1), (1, 0), (-1, 0)  
class Solution:
    # 倒序 + 并查集
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def map_idx(r, c):
            return r * col + c
        
        top, bottom = row * col, row * col + 1
        UF = UnionFind(row * col + 2)

        g = [[0] * col for _ in range(row)]

        for i in range(len(cells) - 1, -1, -1):
            r, c = cells[i]
            r -= 1
            c -= 1
            idx = map_idx(r, c)
            g[r][c] = 1

            if r == 0:
                UF.merge(idx, top)
            
            if r == row - 1:
                UF.merge(idx, bottom)

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and g[nr][nc]:
                    UF.merge(idx, map_idx(nr, nc))

            if UF.is_same(top, bottom):
                return i    # 359ms
                    

class Solution:
    # 对偶问题：是否存在一条从 第一列 到 最后一列 的 水域 防线？
    # 作者：wxyz
    # 链接：https://leetcode.cn/problems/last-day-where-you-can-still-cross/solutions/3869904/si-jie-zheng-xiang-er-fen-dfsbfs-fan-xia-1rho/
    def latestDayToCross(self, m: int, n: int, cells: List[List[int]]) -> int:
        # 切记 8 个方向
        DIRS = (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)

        # 0：陆地
        # 1：孤立或未连接到左边界的水域
        # 2：已连接到最左侧第一列的水域
        state = [[0] * n for _ in range(m)]

        # 能否从左侧第一列到达第 c 列
        def can_reach_from_left(r, c):
            if c == 0:  # 已经是第一列
                return True
            for dx, dy in DIRS:
                x, y = r + dx, c + dy
                if 0 <= x < m and 0 <= y < n and state[x][y] == 2:
                    return True
            return False

        def dfs(r, c):
            if c == n - 1:
                return True
            state[r][c] = 2  # 感染
            for dx, dy in DIRS:
                x, y = r + dx, c + dy
                if 0 <= x < m and 0 <= y < n and state[x][y] == 1 and dfs(x, y):
                    return True
            return False

        for day, (r, c) in enumerate(cells):
            r -= 1  # 下标记得 -1
            c -= 1
            state[r][c] = 1  # 未被感染的水
            if can_reach_from_left(r, c) and dfs(r, c):
                return day


