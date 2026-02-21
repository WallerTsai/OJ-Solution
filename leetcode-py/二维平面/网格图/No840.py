from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        def check(i, j):
            if set([grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1],
                       grid[i][j - 1], grid[i][j + 1],
                       grid[i + 1][j - 1], grid[i + 1][j], grid[i + 1][j + 1]]) != {1, 2, 3, 4, 6, 7, 8, 9}:
                return False
            
            col_2 = grid[i - 1][j] + grid[i + 1][j]
            row_2 = grid[i][j - 1] + grid[i][j + 1]
            if col_2 != 10 or row_2 != 10:
                return False
            
            dia_1 = grid[i - 1][j - 1] + grid[i + 1][j + 1]
            dia_2 = grid[i + 1][j - 1] + grid[i - 1][j + 1]
            if dia_1 != 10 or dia_2 != 10:
                return False
            
            row_1 = grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1]
            row_3 = grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1]
            if row_1 != 15 or row_3 != 15:
                return False
            
            col_1 = grid[i - 1][j - 1] + grid[i][j - 1] + grid[i + 1][j - 1]
            col_3 = grid[i - 1][j + 1] + grid[i][j + 1] + grid[i + 1][j + 1]
            if col_1 != 15 or col_3 != 15:
                return False
            
            return True
        

        m, n = len(grid), len(grid[0])
        if m < 3 or n < 3:
            return 0
        ans = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 5 and check(i, j):
                    ans += 1

        return ans  # 暴力
    


