from collections import Counter


class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        cnt = Counter(t)
        ans = ''
        for ch in s:
            if ch == '1' and cnt['0'] > 0:
                ans += '1'
                cnt['0'] -= 1
            elif ch == '0' and cnt['1'] > 0:
                ans += '1'
                cnt['1'] -= 1
            else:
                ans += '0'
                cnt[ch] -= 1
        return ans


