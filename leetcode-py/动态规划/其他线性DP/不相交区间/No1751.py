from bisect import bisect_right
from functools import cache
from typing import List


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:

        events.sort()
        n = len(events)

        @cache
        def dfs(i: int, k: int):
            if i == n or k == 0:
                return 0
            
            not_choose = dfs(i + 1, k)

            nx_i = i + 1
            while nx_i < n and events[nx_i][0] <= events[i][1]:
                nx_i += 1
            
            choose = events[i][2] + dfs(nx_i, k - 1)

            return max(not_choose, choose)


        return dfs(0, k)    # 1243ms
    

class Solution:
    # 加上二分
    def maxValue(self, events: List[List[int]], k: int) -> int:

        events.sort()
        n = len(events)

        @cache
        def dfs(i: int, k: int):
            if i == n or k == 0:
                return 0
            
            not_choose = dfs(i + 1, k)

            nx_i = bisect_right(events,events[i][1],key=lambda x: x[0])
            
            choose = events[i][2] + dfs(nx_i, k - 1)

            return max(not_choose, choose)


        return dfs(0, k)    # 1745ms


class Solution:
    # 定义dp[i][k] 前 i 个会议中，最多选 j 个后得到的最大价值
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1]) # 注意这里需要按照结束时间排序
        n = len(events)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            start, end, val = events[i - 1]

            pre = bisect_right(events, start-1, key=lambda x: x[1])

            for j in range(1, k + 1):
                # 不选
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
                # 选
                dp[i][j] = max(dp[i][j], dp[pre][j - 1] + val)

        return dp[-1][-1]   # 835ms


class Solution:
    # 定义dp[i][k] 前 i 个会议中，最多选 j 个后得到的最大价值
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1]) # 注意这里需要按照结束时间排序
        n = len(events)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            start, end, val = events[i - 1]

            pre = bisect_right(events, start-1, hi=i, key=lambda x: x[1])
            for j in range(1, k + 1):
                # 不选
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
                # 选
                dp[i][j] = max(dp[i][j], dp[pre][j - 1] + val)

        return dp[-1][-1]   # 835ms