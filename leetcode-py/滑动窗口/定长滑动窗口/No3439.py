from collections import deque
from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        ans =  0
        startTime += [eventTime]
        endTime = [0] + endTime
        li = deque()
        for s, e in zip(startTime, endTime):
            li.append(s - e)
            if len(li) > k + 1:
                li.popleft()
            ans = max(sum(li), ans)
        return ans  # 超时

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        ans =  0
        startTime += [eventTime]
        endTime = [0] + endTime
        li = []
        for s, e in zip(startTime, endTime):
            li.append(s - e)
            
        left = 0
        cur_sum = 0
        for right, num in enumerate(li):
            cur_sum += num
            if right - left + 1 > k + 1:
                cur_sum -= li[left]
                left += 1
            ans = max(ans, cur_sum)
        return ans  # 80ms