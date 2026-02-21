class Solution:
    def maxPower(self, s: str) -> int:
        ans = i = 0
        n = len(s)
        while i < n:
            start = i
            i += 1
            while i < n and s[i] == s[i - 1]:
                i += 1
            ans = max(ans, i - start)
        return ans