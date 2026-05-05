from bisect import bisect_right
from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        li = []
        ans = []
        for x in obstacles:
            i = bisect_right(li, x)
            if i == len(li):
                li.append(x)
            else:
                li[i] = x
            ans.append(i + 1)
        return ans


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        dp = [1] * n 
        for i in range(n):
            for j in range(i):
                if obstacles[j] <= obstacles[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp   # 超时
