from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        ans = []

        for k in range(n + m - 1):
            if k % 2:
                for j in range(min(k, m - 1), -1, -1):
                    i = k - j
                    if i >= n:
                        break
                    ans.append(mat[k - j][j])
            else:
                for i in range(min(k, n - 1), -1, -1):
                    j = k - i
                    if j >= m:
                        break
                    ans.append(mat[i][k - i])

        return ans  # 13ms

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        ans = []
        for k in range(n + m - 1):
            min_j = max(k - n + 1, 0)
            max_j = min(k, m - 1)
            if k % 2 == 0:  # 偶数从左到右
                for j in range(min_j, max_j + 1):
                    ans.append(mat[k - j][j])
            else:  # 奇数从右到左
                for j in range(max_j, min_j - 1, -1):
                    ans.append(mat[k - j][j])
        return ans