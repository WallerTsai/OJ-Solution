from typing import List


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        diag_num = [[0] * (n + 1) for _ in range(m + 1)]    # ↘ 前缀和
        anti_num = [[0] * (n + 1) for _ in range(m + 1)]    # ↙ 前缀和
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                diag_num[i + 1][j + 1] = diag_num[i][j] + x
                anti_num[i + 1][j] = anti_num[i][j + 1] + x # 注意这里
                # 个人理解
                # 最初的状态转移是
                # diag_num[i][j] = diag_num[i - 1][j - 1] + grid[i][j]  
                # 表示从矩阵最上边或最左边出发，向右下↘到 (i,j)，这条线段的元素和
                # anti_num[i][j] = anti[i - 1][j + 1] + grid[i][j]
                # 表示从矩阵最上边或最右边出发，向左下↙到 (i,j)，这条线段的元素和
                # 根据灵神的前缀和定义，下面这些下标 + 1
                # i - 1 -> i    j - 1 -> j

        def get_diag_sum(x, y, k):
            return diag_num[x + k][y + k] - diag_num[x][y]
        
        def get_anti_sum(x, y, k):
            return anti_num[x + k][y + 1 - k] - anti_num[x][y + 1]
        
        x1 = x2 = x3 = 0
        def update(val: int):
            nonlocal x1, x2, x3
            if val > x1:
                x1, x2, x3 = val, x1, x2
            elif x1 > val > x2:
                x2, x3 = val, x2
            elif x2 > val > x3:
                x3 =val

        # 根据leetcode 官方提示：这里菱形中心坐标和水平宽度可以决定有个菱形
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                # i-k >= 0 且 i+k <= m-1，所以 k <= min(i, m-1-i)，对于 j 同理
                update(x)
                mx = min(i, m - 1 - i, j, n - 1 - j)
                for k in range(1, mx + 1):

                    a = get_diag_sum(i - k, j, k + 1)   # 菱形右上的边
                    b = get_anti_sum(i, j + k, k + 1)   # 菱形右下的边
                    c = get_diag_sum(i, j - k, k + 1)   # 菱形左下的边
                    d = get_anti_sum(i - k, j, k + 1)   # 菱形左上的边
                    # 每条边交点重复统计一次
                    val = a + b + c + d - grid[i - k][j] - grid[i][j + k] - grid[i][j - k] - grid[i + k][j]
                    update(val)

        ans = [x1, x2, x3]
        return [x for x in ans if x > 0]
