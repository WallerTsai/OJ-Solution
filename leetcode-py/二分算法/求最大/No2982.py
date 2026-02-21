from collections import defaultdict
from itertools import groupby


class Solution:
    # 二分 + 滑动窗口计数
    def maximumLength(self, s: str) -> int:
        def check(x:int) -> bool:
            cnt = defaultdict(int)
            left = 0
            for right,value in enumerate(s):
                if value != s[left]:
                    left = right
                if right-left + 1 == x:
                    cnt[value] += 1
                    left += 1
            return max(cnt.values()) >= 3 if cnt else False

        n = len(s)
        l,r = 0,n
        while l < r:
            mid = (l + r + 1) // 2
            # 这里的+1要好好理解
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l if l != 0 else -1   # 5373ms

class Solution:
    def maximumLength(self, s: str) -> int:
        def check(x:int) -> bool:
            cnt = defaultdict(int)
            left = 0
            for right,value in enumerate(s):
                if value != s[left]:
                    left = right
                if right-left + 1 == x:
                    cnt[value] += 1
                    left += 1
            return max(cnt.values()) >= 3 if cnt else False
        
        MX = max([len(list(group)) for c,group in groupby(s)])

        n = len(s)
        l,r = 0,MX + 1
        while l < r:
            mid = (l + r + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l if l != 0 else -1  # 4277ms


class Solution:
    # 灵神
    def maximumLength(self, s: str) -> int:
        group = defaultdict(list)
        cnt = 0
        for i,ch in enumerate(s):
            cnt += 1
            if i+1 == len(s) or ch != s[i+1]:
                group[ch].append(cnt)
                cnt = 0

        ans = 0
        for a in group.values():
            a.sort(reverse=True)
            a.extend([0,0]) # 保证还有两个空
            ans = max(ans,a[0]-2,min(a[0]-1,a[1]),a[2]) # 3种情况最大值

        return ans if ans else -1   # 479ms





