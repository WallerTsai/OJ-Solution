from typing import List


inf = 10 ** 15
fmax = lambda x, y: x if x > y else y
class Solution:
    # 羊神
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        accs = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(n):
                accs[j+1][i+1] = grid[i][j]

        for i in range(n):
            for j in range(n):
                accs[i+1][j+1] += accs[i+1][j]
        
        dp1 = [0] * (n + 1)
        dp2 = [-inf] * (n + 1)
        
        for i in range(1, n + 1):
            ndp1 = [0] * (n + 1)
            ndp2 = [-inf] * (n + 1)
            
            for j in range(n + 1):
                for k in range(j, n + 1):
                    ndp1[k] = fmax(ndp1[k], dp1[j] + accs[i-1][k] - accs[i-1][j])
                for k in range(j + 1):
                    ndp2[k] = fmax(ndp2[k], dp2[j] + accs[i][j] - accs[i][k])
            # 一种情况：空了两列——此时这一行从 0 起步，ndp1[0]
            # 另一种情况：空了一列——此时这一行是 n 行起手，ndp[n] (前面做了交换 n,m 操作)
            ndp1[0] = fmax(ndp1[0], dp2[0])
            ndp1[n] = fmax(ndp1[n], dp2[0])
            # 这里是转移回递减的情况：从满了的增长变为减少
            ndp2[n] = fmax(ndp2[n], ndp1[n])
            dp1, dp2 = ndp1, ndp2
        return max(max(dp1), max(dp2))

