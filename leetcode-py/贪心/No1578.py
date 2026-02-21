from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = pre = 0
        for i, color in enumerate(colors[1:], start=1):
            if color == colors[pre]:
                if neededTime[i] >= neededTime[pre]:
                    ans += neededTime[pre]
                    pre = i
                else:
                    ans += neededTime[i]
            else:
                pre = i
        return ans


# 2026年1月26日
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = pre = 0
        n = len(neededTime)
        for i in range(1, n):
            if colors[i] != colors[pre]:
                pre = i
                continue
            if neededTime[i] >= neededTime[pre]:
                ans += neededTime[pre]
                pre = i
            else:
                ans += neededTime[i]
        return ans
