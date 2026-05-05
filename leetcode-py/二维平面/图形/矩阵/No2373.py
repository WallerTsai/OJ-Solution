from collections import deque
from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[None] * (n - 2) for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                res[i][j] = max(max(row[j: j + 3]) for row in grid[i: i + 3])
        return res




class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        a = b = 3

        res = [[None] * (m - b + 1) for _ in range(n - a + 1)]

        def get_sliding_max(arr, window_size):
            q = deque()
            res = []
            for i, x in enumerate(arr):
                if q and q[0] < i - window_size + 1:
                    q.popleft()
                while q and arr[q[-1]] <= x:
                    q.pop()
                q.append(i)
                if i >= window_size - 1:
                    res.append(arr[q[0]])
            return res
        
        # 横向压缩
        row_max = []    # n * (m - b + 1)
        for row in grid:
            row_max.append(get_sliding_max(row, b))

        l = len(row_max[0])
        for c in range(l):
            col_data = [row_max[r][c] for r in range(n)]
            col_max = get_sliding_max(col_data, a)
            for r in range(n - a + 1):
                res[r][c] = col_max[r]

        return res
    


import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

class Solution:
    def largestLocalRect_IndustryCode(self, grid: list[list[int]], a: int, b: int) -> list[list[int]]:
        arr = np.array(grid)
        windows = sliding_window_view(arr, window_shape=(a, b))
        
        return windows.max(axis=(-2, -1)).tolist()
    


from collections import deque

class Solution:
    def largestLocal(self, grid: list[list[int]], a: int = 3, b: int = 3) -> list[list[int]]:
        def slide_max_rows(mat, k):
            res = []
            for row in mat:
                q = deque()
                curr = []
                for i, val in enumerate(row):
                    if q and q[0] <= i - k: 
                        q.popleft()
                    while q and row[q[-1]] <= val: 
                        q.pop()
                    q.append(i)
                    if i >= k - 1: 
                        curr.append(row[q[0]])
                res.append(curr)
            return res

        mat = slide_max_rows(grid, b)
        mat = list(zip(*mat))
        mat = slide_max_rows(mat, a)
        
        return [list(row) for row in zip(*mat)]