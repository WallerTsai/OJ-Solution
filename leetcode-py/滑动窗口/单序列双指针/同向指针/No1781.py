from typing import Counter


class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            cnt = Counter()
            mx = 0
            for j in range(i, len(s)):
                cnt[s[j]] += 1
                mx = max(mx, cnt[s[j]])
                res += mx - min(cnt.values())
        return res
    
class Solution:
    # 维护最大最小值, 使用fcnt
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            maxi, mini = 0, 0
            cnt = Counter()  # count of each char
            fcnt = Counter() # count of each frequence
            for j in range(i, n):
                c = s[j]
                if cnt[c] == 0:
                    # new minimum
                    mini = 1
                elif cnt[c]==mini and fcnt[cnt[c]] == 1:
                    # mini increased
                    mini += 1
                fcnt[cnt[c]] -= 1
                cnt[c] += 1
                fcnt[cnt[c]] += 1
                maxi = max(maxi, cnt[c])
                ans += maxi - mini
        return ans
