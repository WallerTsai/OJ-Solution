class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        ans = 0
        for ch in s:
            if ch == "a":
                ans += 1
            else:
                ans -= 1
        return abs(ans)