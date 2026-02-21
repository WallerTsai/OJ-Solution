from math import inf
from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort()
        ans = 0
        st = []
        for x, y in points:
            while st and st[-1][1] >= y:
                ans += 1
                st.pop()
            st.append((x, y))

        return ans  # 错误
    
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        ans = 0
        n = len(points)
        for i in range(1,n):
            cur_x, bottom_y = points[i]
            top_y = inf
            for j in range(i - 1, -1, -1):
                x, y = points[j]
                if x > cur_x:
                    continue
                if bottom_y <= y < top_y:
                    ans += 1
                    top_y = y
        return ans  # 11ms

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))  # x 升序，y 降序
        ans = 0
        for i, (_, y1) in enumerate(points):
            max_y = -inf
            for (_, y2) in points[i + 1:]:
                if y1 >= y2 > max_y:
                    max_y = y2
                    ans += 1
        return ans

