from heapq import heappush, heapreplace
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        h = []
        cur_day = 0
        for d, l in courses:
            if cur_day + d <= l:
                cur_day += d
                heappush(h,-d)  # 最大堆
            elif h and d < -h[0]: # 当无法完成这课程 但是比前的最长课程短
                cur_day -= -heapreplace(h,-d) - d
        return len(h)




