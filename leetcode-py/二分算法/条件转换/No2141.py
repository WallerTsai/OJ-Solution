from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:

        batteries.sort(reverse=True)
        total = sum(batteries)
        x = sum(batteries[n - 1: ])
        
        return min(total // n, x)   # 错误
    

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort(reverse=True)
        hq = batteries[: n]
        heapify(hq)
        for b in batteries[n:]:
            MN = heappop(hq)
            heappush(hq, MN + b)
        MN = heappop(hq)
        return max(MN, sum(batteries) // n) # 错误
    

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        m = len(batteries)
        avg = sum(batteries) // n
        idx = bisect_right(batteries, avg)
        num1 = m - idx
        l = n - num1
        l_total = sum(batteries[:idx])
        return min(l_total // l, avg)   # 错误


class Solution:
    # 二分
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 1, sum(batteries) // n + 1
        while left < right:
            mid = (left + right) // 2
            if mid * n <= sum(min(b, mid) for b in batteries):
                left = mid + 1
            else:
                right = mid

        return left - 1 # 1796ms


class Solution:
    # 二分
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 1, sum(batteries) // n + 1
        while left < right:
            mid = (left + right + 1) // 2
            if mid * n <= sum(min(b, mid) for b in batteries):
                left = mid
            else:
                right = mid - 1

        return left # 1453ms
    

class Solution:
    # 排序 + 贪心
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort(reverse=True)
        cur_total = sum(batteries)
        cur_need = n
        for b in batteries:
            if b <= cur_total // cur_need:
                return cur_total // cur_need
            cur_total -= b
            cur_need -= 1   # 67ms

        