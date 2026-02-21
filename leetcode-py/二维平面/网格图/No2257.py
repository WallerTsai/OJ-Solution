from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        cell_set = set()
        walls_set = set((x, y) for x, y in walls)

        for x, y in guards:

            cell_set.add((x, y))

            t_x = x - 1
            while t_x >= 0:
                if (t_x, y) in walls_set:
                    break
                cell_set.add((t_x, y))
                t_x -= 1

            t_x = x + 1
            while t_x < m:
                if (t_x, y) in walls_set:
                    break
                cell_set.add((t_x, y))
                t_x += 1

            t_y = y - 1
            while t_y >= 0:
                if (x, t_y) in walls_set:
                    break
                cell_set.add((x, t_y))
                t_y -= 1

            t_y = y + 1
            while t_y < n:
                if (x, t_y) in walls_set:
                    break
                cell_set.add((x, t_y))
                t_y += 1

        return m * n - len(cell_set) - len(walls)   # 超时
    

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        cell_set = set()
        walls_set = set((x, y) for x, y in walls)
        direction = (0,1),(1,0),(0,-1),(-1,0)
        for dx, dy in direction:
            temp_set = set()
            for x, y in guards:
                if (x, y) in temp_set:
                    continue
                temp_set.add((x, y))
                nx, ny = x + dx, y + dy
                while 0 <= nx < m and 0 <= ny < n:
                    if (nx, ny) in temp_set or (nx, ny) in walls_set:
                        break
                    temp_set.add((nx, ny)) 
                    nx += dx
                    ny += dy
            cell_set.update(temp_set)

        return m * n - len(cell_set) - len(walls)   # 1023ms



# 左右上下
DIRS = (0, -1), (0, 1), (-1, 0), (1, 0)

class Solution:
    # 灵神
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guarded = [[0] * n for _ in range(m)]

        # 标记警卫格子、墙格子
        for x, y in guards:
            guarded[x][y] = -1
        for x, y in walls:
            guarded[x][y] = -1

        # 遍历警卫
        for x0, y0 in guards:
            # 遍历视线方向（左右上下）
            for dx, dy in DIRS:
                # 视线所及之处，被保卫
                x, y = x0 + dx, y0 + dy
                while 0 <= x < m and 0 <= y < n and guarded[x][y] != -1:
                    guarded[x][y] = 1  # 被保卫
                    x += dx
                    y += dy

        # 统计没被保卫（值为 0）的格子数
        return sum(row.count(0) for row in guarded) # 247ms



fun = Solution()
fun.countUnguarded(3, 3, [[1,1]], [[0,1],[1,0],[2,1],[1,2]])