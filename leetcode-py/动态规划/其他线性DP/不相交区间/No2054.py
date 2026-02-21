from bisect import bisect_left, bisect_right
from collections import defaultdict
from functools import cache
from heapq import heappop, heappush
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        dp_map = defaultdict(int)
        sorted_li = []
        events.sort(key=lambda x: x[1])
        
        dp_map[0] = 0
        sorted_li.append(0)

        ans = 0
        for l, r, v in events:
            i = bisect_right(sorted_li, l - 1) - 1
            k = sorted_li[i]
            nv = v + dp_map[k]
            if r in dp_map:
                if dp_map[r] < nv:
                    dp_map[r] = nv
                    ans = max(ans, nv)
            else:
                dp_map[r] = nv
                sorted_li.append(r)
                ans = max(ans, nv)

        return ans  # 仔细审题 最多参加两个时间不重叠的活动
    

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        dp_map = defaultdict(int)
        sorted_li = []
        events.sort(key=lambda x: x[1])
        
        dp_map[0] = 0
        sorted_li.append(0)

        ans = 0
        for l, r, v in events:
            i = bisect_right(sorted_li, l - 1) - 1
            k = sorted_li[i]
            x = v + dp_map[k]
            ans = max(ans, x)

            if r not in dp_map:
                dp_map[r] = max(v, dp_map[sorted_li[-1]])
                sorted_li.append(r)
            elif r in dp_map and dp_map[r] < x:
                dp_map[r] = x
        
        return ans  # 错误
    
class Solution:
    # AI改
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # 按结束时间排序
        events.sort(key=lambda x: x[1])
        
        # 存储 (结束时间, 到该时间为止的最大价值)
        ends = [(0, 0)]  # (结束时间, 最大价值)
        
        ans = 0
        
        for l, r, v in events:
            # 找到最后一个结束时间 < l 的活动
            idx = bisect_right(ends, (l - 1, float('inf'))) - 1
            # 当前活动 + 之前的最佳活动
            ans = max(ans, v + ends[idx][1])
            
            # 更新 ends
            if ends[-1][1] < v:
                if ends[-1][0] == r:
                    # 相同结束时间，更新最大值
                    ends[-1] = (r, v)
                else:
                    ends.append((r, v))
            elif ends[-1][0] < r:
                # 新的结束时间，继承前一个最大值
                ends.append((r, ends[-1][1]))
        
        return ans
    
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort(key=lambda x: x[1])
        @cache
        def dfs(i: int, pre: int):
            if i == n:
                return 0
            
            l, r, x = events[i]
            if pre > l:
                return dfs(i + 1, pre)
            
            return max(x, dfs(i + 1, pre))
            
        ans = 0
        for i in range(n):
            l, r, v = events[i]
            ans = max(ans, v + dfs(i + 1, r + 1))

        dfs.cache_clear()
        return ans  # 超时
            

class Solution:
    # 前缀最大值 + 二分查找
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort(key=lambda x: x[1])

        pre_max = [0]
        for i in range(n):
            pre_max.append(max(pre_max[-1], events[i][2]))

        sorted_r = [x[1] for x in events]
        sorted_r = [0] + sorted_r

        ans = 0
        for i in range(n):
            l, r, v = events[i]
            idx = bisect_left(sorted_r, l) - 1
            ans = max(ans, v + pre_max[idx])
        
        return ans  # 240ms


class Solution:
    # 最小堆
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        hq = []
        max_pre = 0 # 用最小堆来维护前一活动的最大值

        ans = 0
        for l, r, v in events:
            while hq and hq[0][0] < l:
                _, x = heappop(hq)
                max_pre = max(max_pre, x)
            ans = max(ans, max_pre + v)
            heappush(hq,(r, v))
        
        return ans  # 183ms
    

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

        return dp[-1][-1]
    
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        return self.maxValue(events, 2) # 740ms
    

class Solution:
    # 单调栈 + 二分
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])
        st = [(0, 0)]
        ans = 0
        for l, r, v in events:
            i = bisect_left(st, (l, )) - 1
            ans = max(ans, v + st[i][1])
            if v > st[-1][1]:
                st.append((r, v))
        return ans  # 197ms


class Solution:
    # 作者：wxyz
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # 按开始时间排序，作为 “当前第二个” 活动
        start_sort = sorted(events, key=lambda x: x[0])
        # 按结束时间排序，作为 “之前第一个” 活动
        end_sort = sorted(events, key=lambda x: x[1])
        # 已经结束的活动中的最大价值
        max_prev = 0
        ans = 0
        # 在 end_sort 中移动
        i = 0
        n = len(events)
        
        # 第二个活动
        for s, e, v in start_sort:
            # 找出所有在当前活动开始时间 s 之前结束的活动
            while i < n and end_sort[i][1] < s:
                if end_sort[i][2] > max_prev:
                    max_prev = end_sort[i][2]
                i += 1
            
            # 更新最大
            if max_prev + v > ans:
                ans = max_prev + v
        
        return ans


fun = Solution()
fun.maxTwoEvents([[10,83,53],[63,87,45],[97,100,32],[51,61,16]])
