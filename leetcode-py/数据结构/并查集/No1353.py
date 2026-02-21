from bisect import bisect_left
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        start = -1
        ans = 0
        for l, r in events:
            if l > start:
                ans += 1
                start = l
            elif start >= r:
                continue
            else:
                start += 1
                ans += 1
        return ans  # 错误
    
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x : x[1])
        start = -1
        ans = 0
        for l, r in events:
            if l > start:
                ans += 1
                start = l
            elif start >= r:
                continue
            else:
                start += 1
                ans += 1
        return ans  # 错误
    

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x : (x[1] - x[0]))
        callendar = [-1]
        length = 1
        for l, r in events:
            i = bisect_left(callendar,l)
            if i == length:
                callendar.append(l)
                length += 1
            else:
                start = l
                while start <= r and i < length:
                    if start == callendar[i]:
                        start += 1
                        i += 1
                    else:
                        callendar.append(start)
                        length += 1
                        break
                if i == length and start <= r:
                    callendar.append(start)
                    length += 1
            callendar.sort()
        return length - 1   # 错误
    
class Solution:
    # 并查集
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])
        mx = events[-1][1]
        fa = list(range(mx + 2))

        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]
        
        ans = 0
        for l, r in events:
            x = find(l)
            if x <= r:
                ans += 1
                fa[x] = x + 1
        
        return ans





fun = Solution()
fun.maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]])