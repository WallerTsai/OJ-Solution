from typing import List

# 枚举对角线 + 前后缀分解
class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        st = set()

        # k = i - j + n
        for k in range(1,m + n):
            min_j = max(n - k, 0)
            max_j = min(m + n - 1 - k, n - 1)

            # 前缀
            st.clear()
            for j in range(min_j,max_j + 1):
                i = k + j - n
                ans[i][j] = len(st)
                st.add(grid[i][j])
            
            # 后缀
            st.clear()
            for j in range(max_j, min_j - 1, -1):
                i = k + j - n
                ans[i][j] = abs(ans[i][j] - len(st))
                st.add(grid[i][j])
            
        return ans