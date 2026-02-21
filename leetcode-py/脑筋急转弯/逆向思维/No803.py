from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]

    def get_size(self, x: int) -> int:
        return self.size[self.find(x)]
    
    def is_same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
DIRS = (0, 1), (0, -1), (1, 0), (-1, 0)  
fmax = lambda x, y : x if x > y else y
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        def get_idx(r, c):
            return r * n + c
        
        invaild_set = set()
        for i, (r, c) in enumerate(hits):
            if grid[r][c] == 0:
                invaild_set.add(i)
                continue
            grid[r][c] = 0 

        UF = UnionFind(m * n + 1)
        top = m * n

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue

                idx = get_idx(r, c)
                if r == 0:
                    UF.merge(idx, top)
                if r > 0 and grid[r - 1][c] == 1:
                    UF.merge(idx, get_idx(r - 1, c))
                if c > 0 and grid[r][c - 1] == 1:
                    UF.merge(idx, get_idx(r, c - 1))

        res = [0] * len(hits)

        for i in range(len(hits) - 1, -1, -1):

            if i in invaild_set:
                continue

            r, c = hits[i]

            pre = UF.get_size(top)

            idx = get_idx(r, c)
            if r == 0:
                UF.merge(idx, top)

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    UF.merge(idx, get_idx(nr, nc))

            cur = UF.get_size(top)

            res[i] = fmax(0, cur - pre - 1)
            grid[r][c] = 1

        return res

fun = Solution().hitBricks([[1,0,0,0],[1,1,1,0]], [[1,0]])


class Solution:
    # lc最快
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        # 逆序遍历
        def dfs(i,j):
            # 返回感染的区域数量

            grid[i][j] = 2  # 已被感染的标志
            count = 1

            if i > 0 and grid[i - 1][j] == 1:
                count += dfs(i - 1,j)
            if i < m - 1 and grid[i + 1][j] == 1:
                count += dfs(i + 1,j)
            if j > 0 and grid[i][j - 1] == 1:
                count += dfs(i,j - 1)
            if j < n - 1 and grid[i][j + 1] == 1:
                count += dfs(i,j + 1)
            
            return count

        m,n,hlen = len(grid),len(grid[0]),len(hits)

        for x,y in hits:
            grid[x][y] -= 1
        
        for j in range(n):
            if grid[0][j] == 1:
                dfs(0,j)  # 感染第一行
        
        ans = [0] * hlen

        for hitP in range(hlen - 1,-1,-1):
            # 逆序遍历补齐砖块
            i,j = hits[hitP]
            grid[i][j] += 1
            if grid[i][j] == 1 and (i == 0 or (i > 0 and grid[i - 1][j] == 2) or (i < m - 1 and grid[i + 1][j] == 2) or (j > 0 and grid[i][j - 1] == 2) or (j < n - 1 and grid[i][j + 1] == 2)):
                # 这个格子新增，且连接到感染的格子
                ans[hitP] = dfs(i,j) - 1  # 自己这一格不算新增
            # else:
            #     ans[hitP] = 0

        return ans