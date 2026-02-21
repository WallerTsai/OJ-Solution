from typing import List


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()

        h = v = 1
        l = 1
        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i - 1] + 1:
                l += 1
                if l > h:
                    h = l
            else:
                l = 1

        l = 1
        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i - 1] + 1:
                l += 1
                if l > v:
                    v = l
            else:
                l = 1

        return pow(min(h, v) + 1, 2)


class Solution:
    # No128
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        n = 0
        for num in nums:
            if num - 1 in nums:
                continue

            nx = num + 1
            while nx in nums:
                nx += 1

            n = max(n, nx - num)

        return n
    
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        h = self.longestConsecutive(hBars)
        v = self.longestConsecutive(vBars)
        return pow(min(h, v) + 1, 2)    # 0ms

Solution().maximizeSquareHoleArea(3, 2, [3,2,4], [3,2])