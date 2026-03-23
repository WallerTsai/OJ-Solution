from math import inf
from typing import List


class Solution:
    # 贪心
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        ans = 0
        right = 0
        n = len(clips)
        i = 0
        while i < n:
            if right >= time:
                break
            l = right
            j = i
            while j < n and clips[j][0] <= right:
                l = max(l, clips[j][1])
                j += 1
            if i == j:
                return -1
            
            right = l
            i = j
            ans += 1
        return ans if right >= time else -1
        

class Solution:
    # No55
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        s = [0] * time
        for l, r in clips:
            if l < time:
                s[l] = max(s[l], r)

        ans = mx = pre = 0
        for i, t in enumerate(s):
            mx = max(mx, t)
            if i >= mx:
                return -1

            if i == pre:
                ans += 1
                pre = mx

        return ans
    
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        s = [0] * time
        for l, r in clips:
            if l < time:
                s[l] = max(s[l], r)

        ans = mx = pre = 0
        for i, t in enumerate(s):
            if i > mx:
                return -1

            mx = max(mx, t)
            if i == pre:
                ans += 1
                pre = mx

        return ans if mx >= time else -1
    

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # 令 dp[i] 表示将区间 [0,i) 覆盖所需的最少子区间的数量
        dp = [inf] * (time + 1)
        dp[0] = 0
        for i in range(1, time + 1):
            for l, r in clips:
                if l < i <= r:
                    dp[i] = min(dp[i], dp[l] + 1)
        return -1 if dp[time] == inf else dp[time]
