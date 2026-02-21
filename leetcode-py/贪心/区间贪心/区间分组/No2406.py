from sortedcontainers import SortedList # type: ignore
from heapq import heappush, heapreplace
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        ans = 0
        n = len(intervals)
        stack = []
        intervals.sort(key= lambda x: x[1])
        while n:
            pre_right = 0
            for l, r in intervals:
                if l > pre_right:
                    pre_right = r
                    n -= 1
                else:
                    stack.append([l,r])

            ans += 1
            intervals = stack[:]
            stack.clear()
        return ans  # 策略有问题
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        ans = 0
        n = len(intervals)
        stack = []
        intervals.sort(key= lambda x: x[0])
        while n:
            pre_right = 0
            for l, r in intervals:
                if l > pre_right:
                    pre_right = r
                    n -= 1
                else:
                    stack.append([l,r])

            ans += 1
            intervals = stack[:]
            stack.clear()
        return ans  # 超时

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[0])
        bucket = []
        for l ,r in intervals:
            if bucket and bucket[0] < l:
                bucket[0] = r
            else:
                bucket.append(r)
            bucket.sort()
        return len(bucket)  # 超时

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[0])
        bucket = SortedList()
        for l ,r in intervals:
            if bucket and bucket[0] < l:
                del bucket[0]
                bucket.add(r)
            else:
                bucket.add(r)
        return len(bucket)  # 473ms

class Solution:
    # 堆
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        h = []
        for left, right in intervals:
            if h and left > h[0]:
                heapreplace(h, right)
            else:
                heappush(h, right)
        return len(h)

fun = Solution()
fun.minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]])