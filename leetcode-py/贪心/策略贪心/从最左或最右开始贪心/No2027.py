class Solution:
    def minimumMoves(self, s: str) -> int:
        s = list(s)
        ans, n = 0, len(s)
        for i in range(n):
            if s[i] == "X":
                if i + 1 < n:
                    s[i + 1] = "0"
                if i + 2 < n:
                    s[i + 2] = "0"
                ans += 1
        return ans