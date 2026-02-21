from typing import List


class Solution:
    # 暴力
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        cnt = [0] * (n * n + 1)
        for r in grid:
            for x in r:
                cnt[x] += 1

        ans = [0, 0]
        for i, x in enumerate(cnt):
            if x == 2:
                ans[0] = i
            elif x == 0:
                ans[-1] = i
        
        return ans



class Solution:
    # 灵神
    # https://leetcode.cn/problems/find-missing-and-repeated-values/solutions/2569783/mo-ni-pythonjavacgo-by-endlesscheng-mexz/
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        m = len(grid) ** 2
        # 注：两次遍历可以合并为一次遍历，这里只是为了方便实现用了两次遍历
        d1 = sum(x for row in grid for x in row) - m * (m + 1) // 2
        d2 = sum(x * x for row in grid for x in row) - m * (m + 1) * (m * 2 + 1) // 6
        return [(d2 // d1 + d1) // 2, (d2 // d1 - d1) // 2]