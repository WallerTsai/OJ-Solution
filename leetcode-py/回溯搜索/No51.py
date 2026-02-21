from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        record = [0] * n
        col = [False] * n
        diag1 = [False] * (2 * n - 1)   # 正斜线
        diag2 = [False] * (2 * n - 1)   # 反斜线
        # 递归行
        def dfs(row: int) -> None:
            if row == n:
                ans.append(["." * c + "Q" + "." * (n - 1 - c) for c in record])
                return
            for c,f in enumerate(col):
                if not f and not diag2[row + c] and not diag1[row - c + n - 1]:
                    record[row] = c
                    col[c] = diag2[row + c] = diag1[row - c + n - 1] = True
                    dfs(row + 1)
                    col[c] = diag2[row + c] = diag1[row - c + n - 1] = False

        dfs(0)
        return ans
