from typing import List


class Solution:
    # 暴力
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        length = len(grid)
        for i in range(length):
            nums = []
            row,col = i,0
            while row < length and col < length:
                nums.append(grid[row][col])
                row += 1
                col += 1

            nums.sort(reverse = True)

            row,col = i,0
            index = 0
            while row < length and col < length:
                grid[row][col] = nums[index]
                row += 1
                col += 1
                index += 1

        for j in range(1,length):
            nums = []
            row,col = 0,j
            while row < length and col < length:
                nums.append(grid[row][col])
                row += 1
                col += 1

            nums.sort()

            row,col = 0,j
            index = 0
            while row < length and col < length:
                grid[row][col] = nums[index]
                row += 1
                col += 1
                index += 1
        return grid
    
class Solution:
    # 灵神
    # 枚举对角线模板
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        # 第一排在右上，最后一排在左下
        # 每排从左上到右下
        # 令 k=i-j+n，那么右上角 k=1，左下角 k=m+n-1
        for k in range(1, m + n):
            # 核心：计算 j 的最小值和最大值
            min_j = max(n - k, 0)  # i=0 的时候，j=n-k，但不能是负数
            max_j = min(m + n - 1 - k, n - 1)  # i=m-1 的时候，j=m+n-1-k，但不能超过 n-1
            a = [grid[k + j - n][j] for j in range(min_j, max_j + 1)]  # 根据 k 的定义得 i=k+j-n
            a.sort(reverse=min_j == 0)
            for j, val in zip(range(min_j, max_j + 1), a):
                grid[k + j - n][j] = val
        return grid
    
class Solution:
    # 似乎暴力更快
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for k in range(n):
            tmp = [grid[k + j][j] for j in range(n - k)]
            tmp.sort(reverse = True)
            for j in range(n - k):
                grid[k + j][j] = tmp[j]
        for k in range(1, n):
            tmp = [grid[i][k + i] for i in range(n - k)]
            tmp.sort()
            for i in range(n- k):
                grid[i][k + i] = tmp[i]
        return grid
            


