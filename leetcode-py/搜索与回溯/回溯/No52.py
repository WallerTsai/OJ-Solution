class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        col = [False] * n
        diag1 = [False] * (2 * n - 1)   # 正斜线
        diag2 = [False] * (2 * n - 1)   # 反斜线
        # 递归行
        def dfs(row: int) -> None:
            if row == n:
                nonlocal ans
                ans += 1
                return
            for c,f in enumerate(col):
                if not f and not diag2[row + c] and not diag1[row - c + n - 1]:
                    col[c] = diag2[row + c] = diag1[row - c + n - 1] = True
                    dfs(row + 1)
                    col[c] = diag2[row + c] = diag1[row - c + n - 1] = False

        dfs(0)
        return ans