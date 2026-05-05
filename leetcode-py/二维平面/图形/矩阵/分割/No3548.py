from collections import defaultdict
from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(sum(row) for row in grid)
        cnt = defaultdict(int)
        for row in grid:
            for x in row:
                cnt[x] += 1

        def check(grid: List[List[int]]) -> bool:
            m, n = len(grid), len(grid[0])
            if m < 2:
                return False
            
            pre_cnt = defaultdict(int)
            sub_cnt = cnt.copy()
            pre = 0
            for i in range(m - 1):
                for x in grid[i]:
                    pre += x
                    pre_cnt[x] += 1
                    sub_cnt[x] -= 1
                if pre == total - pre:
                    return True
                
                elif pre > total - pre:
                    val = 2 * pre - total
                    if pre_cnt[val] >= 1:
                        if i == 0:  # 第一行
                            if grid[i][0] == val or grid[i][-1] ==val:
                                return True
                        elif n == 1: # 只有一列，移除两端
                            if grid[0][0] == val or grid[i][0] == val:
                                return True
                        else:
                            return True

                elif pre < total - pre:
                    val = total - 2 * pre
                    if sub_cnt[val] >= 1:
                        if i == m - 2:  # 最后一行
                            if grid[-1][0] == val or grid[-1][-1] == val:
                                return True
                        elif n == 1:
                            if grid[i + 1][0] == val or grid[-1][0] ==val:
                                return True
                        else:
                            return True
            return False
        
        return check(grid) or check(list(zip(*grid)))


class Solution:
    # 灵神
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(sum(row) for row in grid)

        # 能否水平分割
        def check(a: List[List[int]]) -> bool:
            m, n = len(a), len(a[0])

            # 删除上半部分中的一个数，能否满足要求
            def f(a: List[List[int]]) -> bool:
                st = {0}  # 0 对应不删除数字
                s = 0
                for i, row in enumerate(a[:-1]):
                    for j, x in enumerate(row):
                        s += x
                        # 第一行，不能删除中间元素
                        if i > 0 or j == 0 or j == n - 1:
                            st.add(x)
                    # 特殊处理只有一列的情况，此时只能删除第一个数或者分割线上那个数
                    if n == 1:
                        if s * 2 == total or s * 2 - total == a[0][0] or s * 2 - total == row[0]:
                            return True
                        continue
                    if s * 2 - total in st:
                        return True
                    # 如果分割到更下面，那么可以删第一行的元素
                    if i == 0:
                        st.update(row)
                return False

            # 删除上半部分中的数 or 删除下半部分中的数
            return f(a) or f(a[::-1])

        # 水平分割 or 垂直分割
        return check(grid) or check(list(zip(*grid)))