from collections import Counter, defaultdict


class Solution:
    # 大暴力
    def maximumLengthSubstring(self, s: str) -> int:
        length = len(s)
        res = 0
        for i in range(length):
            for j in range(i+1,length+1):
                cnt = Counter(s[i:j])
                if max(cnt.values()) <= 2:
                    res = max(res,j-i)
        return res  # 1096ms

class Solution:
    # 窗口+defaultdict
    def maximumLengthSubstring(self, s: str) -> int:
        cnt = defaultdict(int)
        res = 0
        left = 0
        for i,c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 2:
                cnt[s[left]] -= 1
                left += 1
            if res < i - left + 1:
                res = i - left + 1
        return res  # 3ms
    
class Solution:
# 作者：Make_Hua
    # 哈希表,对字母的Unicode哈希
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        l, r, ans = 0, 0, 0
        mp = [0] * 26
        while r < n:
            mp[ord(s[r]) - ord('a')] += 1  # 入窗
            while mp[ord(s[r]) - ord('a')] == 3:
                mp[ord(s[l]) - ord('a')] -= 1  # 出窗
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans

