from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        cntx = defaultdict(list)
        cnty = defaultdict(list)
        buildings.sort()
        for x, y in buildings:
            cntx[x].append(y)
            cnty[y].append(x)

        ans = 0
        for x, y in buildings:
            i = bisect_left(cntx[x], y)
            if i == 0 or i == len(cntx[x]) - 1:
                continue
            j = bisect_left(cnty[y], x)
            if j == 0 or j == len(cnty[y]) - 1:
                continue
            ans += 1

        return ans  # 828ms
    
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        cntx = defaultdict(list)
        cnty = defaultdict(list)
        buildings.sort()
        for x, y in buildings:
            cntx[x].append(y)
            cnty[y].append(x)

        remove_set = set()
        for x, li in cntx.items():
            remove_set.add((x, li[0]))
            remove_set.add((x, li[-1]))
        
        for y, li in cnty.items():
            remove_set.add((li[0], y))
            remove_set.add((li[-1], y))

        return len(buildings) - len(remove_set) # 848ms
    
class Solution:
    # 灵神
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        row_min = [n + 1] * (n + 1)
        row_max = [0] * (n + 1)
        col_min = [n + 1] * (n + 1)
        col_max = [0] * (n + 1)

        for x, y in buildings:
            # 手写 min max 更快
            if x < row_min[y]: row_min[y] = x
            if x > row_max[y]: row_max[y] = x
            if y < col_min[x]: col_min[x] = y
            if y > col_max[x]: col_max[x] = y

        ans = 0
        for x, y in buildings:
            if row_min[y] < x < row_max[y] and col_min[x] < y < col_max[x]:
                ans += 1
        return ans  # 152ms






fun = Solution()
fun.countCoveredBuildings(3, [[1,1],[1,2],[2,1],[2,2]])