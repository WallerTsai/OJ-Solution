from typing import List

# 一般地，对于整数 k，我们有 (grid[i][j]+kx)modx=grid[i][j]modx。
# 所以操作后，grid[i][j]modx 是不变的。
# 每个数模 x 的结果必须都一样，才能变成同一个数。
# 否则无解，输出 −1。

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        li = []
        t = grid[0][0] % x
        for row in grid:
            for y in row:
                if y % x != t:
                    return -1
                li.append(y)

        li.sort()
        mid = li[len(li) // 2]

        ans = 0
        for y in li:
            ans += abs(y - mid) // x

        return ans