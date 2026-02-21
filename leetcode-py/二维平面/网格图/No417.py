from collections import deque
from functools import cache
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        m, n = len(heights), len(heights[0])

        PO = [[False] * n for _ in range(m)]
        for i in range(m):
            pre = 0
            for j in range(n):
                if heights[i][j] >= pre:
                    PO[i][j] = True
                    pre = heights[i][j]
                else:
                    break
        for j in range(n):
            pre = 0
            for i in range(m):
                if heights[i][j] >= pre:
                    PO[i][j] = True
                    pre = heights[i][j]
                else:
                    break

        AO = [[False] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            pre = 0
            for j in range(n - 1, -1, -1):
                if heights[i][j] >= pre:
                    AO[i][j] = True
                    pre = heights[i][j]
                else:
                    break
        for j in range(n - 1, -1, -1):
            pre = 0
            for i in range(m - 1, -1, -1):
                if heights[i][j] >= pre:
                    AO[i][j] = True
                    pre = heights[i][j]
                else:
                    break

        for i in range(m):
            for j in range(n):
                if PO[i][j] and AO[i][j]:
                    ans.append([i, j])

        return ans  # 错误
    

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        m, n = len(heights), len(heights[0])

        @cache
        def PO_dfs(i, j):
            if i <= 0 or j <= 0:
                return True
            flag = False
            if heights[i - 1][j] <= heights[i][j]:
                flag = PO_dfs(i - 1, j)
            if not flag and heights[i][j - 1] <= heights[i][j]:
                flag = PO_dfs(i, j - 1)
            return flag
        
        @cache
        def AO_dfs(i, j):
            if i >= m - 1 or j >= n - 1:
                return True
            flag = False
            if heights[i + 1][j] <= heights[i][j]:
                flag = AO_dfs(i + 1, j)
            if not flag and heights[i][j + 1] <= heights[i][j]:
                flag = AO_dfs(i, j + 1)
            return flag
        
        for i in range(m):
            for j in range(n):
                if PO_dfs(i, j) and AO_dfs(i, j):
                    ans.append([i, j])

        return ans
    # 错误
    # 输入 [[1,2,3],[8,9,4],[7,6,5]]
    # 输出 [[0,2],[1,0],[1,1],[1,2],[2,0],[2,2]]
    # 预期 [[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        DIR = (1, 0), (0, 1), (-1, 0), (0, -1)
        ans = []
        m, n = len(heights), len(heights[0])

        @cache
        def PO_dfs(i, j):
            if i <= 0 or j <= 0:
                return True
            
            flag = False
            cur = heights[i][j]
            for dx, dy in DIR:
                nx, ny = i + dx, j + dy
                if heights[nx][ny] <= cur:
                    flag = PO_dfs(nx, ny)
                if flag:
                    break

            return flag
        
        @cache
        def AO_dfs(i, j):
            if i >= m - 1 or j >= n - 1:
                return True
            
            flag = False
            cur = heights[i][j]
            for dx, dy in DIR:
                nx, ny = i + dx, j + dy
                if heights[nx][ny] <= cur:
                    flag = AO_dfs(nx, ny)
                if flag:
                    break

            return flag
        
        for i in range(m):
            for j in range(n):
                if PO_dfs(i, j) and AO_dfs(i, j):
                    ans.append([i, j])

        return ans  # 这个多次重复
    

class Solution:
    # BFS
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        DIR = (1, 0), (0, 1), (-1, 0), (0, -1)
        ans = []
        m, n = len(heights), len(heights[0])

        PO = [[False] * n for _ in range(m)]
        queue = deque()
        for j in range(n):
            PO[0][j] = True
            queue.append([0, j])
        for i in range(m):
            PO[i][0] = True
            queue.append([i, 0])

        while queue:
            x, y = queue.popleft()
            cur_h = heights[x][y]
            for dx,dy in DIR:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not PO[nx][ny] and heights[nx][ny] >= cur_h:
                    queue.append([nx,ny])
                    PO[nx][ny] = True

        AO = [[False] * n for _ in range(m)]
        queue.clear()
        for j in range(n):
            AO[m - 1][j] = True
            queue.append([m - 1, j])
        for i in range(m):
            AO[i][n - 1] = True
            queue.append([i, n - 1])

        while queue:
            x, y = queue.popleft()
            cur_h = heights[x][y]
            for dx,dy in DIR:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not AO[nx][ny] and heights[nx][ny] >= cur_h:
                    queue.append([nx,ny])
                    AO[nx][ny] = True

        for i in range(m):
            for j in range(n):
                if PO[i][j] and AO[i][j]:
                    ans.append([i, j])

        return ans  # 31ms
    
class Solution:
    # BFS
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        DIR = (1, 0), (0, 1), (-1, 0), (0, -1)
        ans = []
        m, n = len(heights), len(heights[0])

        PO = [[False] * n for _ in range(m)]
        queue = deque()
        for j in range(n):
            PO[0][j] = True
            queue.append([0, j])
        for i in range(m):
            PO[i][0] = True
            queue.append([i, 0])

        while queue:
            x, y = queue.popleft()
            cur_h = heights[x][y]
            for dx,dy in DIR:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not PO[nx][ny] and heights[nx][ny] >= cur_h:
                    queue.append([nx,ny])
                    PO[nx][ny] = True

        AO = [[False] * n for _ in range(m)]
        queue.clear()
        for j in range(n):
            AO[m - 1][j] = True
            queue.append([m - 1, j])
            if PO[m - 1][j]:
                ans.append([m - 1, j])
        for i in range(m - 1):
            AO[i][n - 1] = True
            queue.append([i, n - 1])
            if PO[i][n - 1]:
                ans.append([i, n - 1])

        while queue:
            x, y = queue.popleft()
            cur_h = heights[x][y]
            for dx,dy in DIR:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not AO[nx][ny] and heights[nx][ny] >= cur_h:
                    queue.append([nx,ny])
                    AO[nx][ny] = True
                    if PO[nx][ny]:
                        ans.append([nx, ny])

        return ans  # 23ms