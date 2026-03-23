from typing import List


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def check(i, j, k):
            target = sum(grid[i][j + a] for a in range(k))

            for r in range(k):
                cur = 0
                for c in range(k):
                    cur += grid[i + r][j + c]
                if cur != target:
                    return False
                
            for c in range(k):
                cur = 0
                for r in range(k):
                    cur += grid[i + r][j + c]
                if cur != target:
                    return False
                
            d1 = 0
            for d in range(k):
                d1 += grid[i + d][j + d]
            if d1 != target:
                return False
            
            d2 = 0
            for d in range(k):
                d2 += grid[i + d][j + k -1 - d]
            if d2 != target:
                return False
            
            return True
        
        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if check(i, j, k):
                        return k
        return 1    # O(m * n * min(m, n)^3)    # 1191ms



class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # 行前缀和
        row_sum = [[0] * (n + 1) for _ in range(m)]
        # 列前缀和
        col_sum = [[0] * n for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                row_sum[i][j + 1] = row_sum[i][j] + grid[i][j]
                col_sum[i + 1][j] = col_sum[i][j] + grid[i][j]

        def check(i, j, k):
            
            d1 = sum(grid[i + d][j + d] for d in range(k))

            d2 = sum(grid[i + d][j + k - 1 - d] for d in range(k))
            if d2 != d1:
                return False
            
            for r in range(k):
                if row_sum[i + r][j + k] - row_sum[i + r][j] != d1:
                    return False
                
            for c in range(k):
                if col_sum[i + k][j + c] - col_sum[i][j + c] != d1:
                    return False
                
            return True
        
        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if check(i, j, k):
                        return k
                    
        return 1    #399ms  # O(m * n * min(m, n)^2)
            


class Solution:
    # 根据灵神代码添加对角线前缀和
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        row_sum = [[0] * (n + 1) for _ in range(m)]
        col_sum = [[0] * n for _ in range(m + 1)]
        diag_sum = [[0] * (n + 1) for _ in range(m + 1)] # 主对角线 ↘
        anti_sum = [[0] * (n + 1) for _ in range(m + 1)] # 副对角线 ↙

        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                # 行：当前 = 左边 + val
                row_sum[i][j + 1] = row_sum[i][j] + val
                # 列：当前 = 上边 + val
                col_sum[i + 1][j] = col_sum[i][j] + val
                # 主对角线：当前 = 左上 + val
                diag_sum[i + 1][j + 1] = diag_sum[i][j] + val
                # 副对角线：当前 = 右上 + val
                # 注意：这里 anti_sum[i][j+1] 对应的是 grid[i-1][j+1] 位置的累积和
                anti_sum[i + 1][j] = anti_sum[i][j + 1] + val

        def check(i, j, k):
            d1 = diag_sum[i + k][j + k] - diag_sum[i][j]
            d2 = anti_sum[i + k][j] - anti_sum[i][j + k]
            
            if d1 != d2:
                return False

            for r in range(k):
                if row_sum[i + r][j + k] - row_sum[i + r][j] != d1:
                    return False
            
            for c in range(k):
                if col_sum[i + k][j + c] - col_sum[i][j + c] != d1:
                    return False
            
            return True
        

        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if check(i, j, k):
                        return k
        
        return 1    # 39ms