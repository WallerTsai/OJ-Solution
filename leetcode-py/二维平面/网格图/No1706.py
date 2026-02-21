from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m,n = len(grid),len(grid[0])
        pos = [x for x in range(n)]
        for i in range(m):
            for l,x in enumerate(pos):
                if x == -1:
                    continue
                if x < n-1 and grid[i][x] == 1 and grid[i][x+1] ==1:
                    pos[l] = x + 1
                elif x > 0 and grid[i][x] == -1 and grid[i][x-1] == -1:
                    pos[l] = x - 1
                else:
                    pos[l] =  -1
        return pos # 3ms
    
class Solution:
    # 这样时间复杂度更小一点
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        ans = [-1] * n
        for j in range(n):
            # 模拟第 j 列球的移动
            cur_col = j  # 当前列号
            for row in grid:
                d = row[cur_col]  # -1 或 1，表示左/右
                cur_col += d  # 左/右走一步
                # 如果球出界或者卡在 V 形，退出循环，否则继续循环（垂直落入下一排）
                # V 形就是 -1 的左边是 1，1 的右边是 -1，即 row[cur_col] != d
                if cur_col < 0 or cur_col == n or row[cur_col] != d:
                    break
            else:  # 没有中途 break，说明球成功到达底部
                ans[j] = cur_col
        return ans