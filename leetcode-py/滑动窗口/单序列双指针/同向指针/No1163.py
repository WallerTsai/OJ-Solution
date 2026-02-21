class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j = 0, 1
        n = len(s)
        while j < n:
            k = 0
            while j + k < n and s[i + k] == s[j + k]:
                k += 1
            if j + k < n and s[i + k] < s[j + k]:
                i, j = j, max(j + 1, i + k + 1)
            else:
                j += k + 1
        return s[i:]
    
# 思路来源 No2653
f = Solution()
f.lastSubstring("cacacb")