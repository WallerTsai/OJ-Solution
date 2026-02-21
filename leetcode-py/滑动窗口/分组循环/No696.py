class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        ans = pre = cur = 0
        for i in range(n):
            cur += 1
            if i == n - 1 or s[i] != s[i + 1]:
                ans += min(pre, cur)
                pre = cur
                cur = 0
        return ans


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = i = pre = 0
        while i < len(s):
            start = i
            i += 1
            while i < len(s) and s[i] == s[i - 1]:
                i += 1
            cur = i - start
            ans += min(pre, cur)
            pre = cur
        return ans



