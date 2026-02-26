class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)
        ans = n - 1
        i = s.rfind("1")
        if i > 0:
            ans += s.count('0', 1, i) + 2
        return ans