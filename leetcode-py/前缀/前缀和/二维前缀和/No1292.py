from typing import List


class Solution:
    # 二维前缀和
    # 调用 No.304
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + x

        def sumRegion(row1: int, col1: int, row2: int, col2: int) -> int:
            return s[row2 + 1][col2 + 1] - s[row2 + 1][col1] - s[row1][col2 + 1] + s[row1][col1]

        l = 0
        for i in range(m):
            for j in range(n):
                while i + l < m and j + l < n and sumRegion(i, j, i + l, j + l) <= threshold:
                    l += 1

        return l    # 103ms
    

class Solution:
    # 二维前缀和 + 二分查找
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + x

        def sumRegion(row1: int, col1: int, row2: int, col2: int) -> int:
            return s[row2 + 1][col2 + 1] - s[row2 + 1][col1] - s[row1][col2 + 1] + s[row1][col1]

        def check(k):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if sumRegion(i, j, i + k - 1, j + k - 1) <= threshold:
                        return True
            return False

        left, right = 0, min(m, n) + 1
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left # 259ms

Solution().maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4)
