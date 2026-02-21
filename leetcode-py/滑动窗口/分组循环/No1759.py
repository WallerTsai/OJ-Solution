MOD = 1_000_000_007
class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = i = 0
        n = len(s)
        while i < n:
            start = i
            i += 1
            while i < n and s[i] == s[i - 1]:
                i += 1
            
            ans = (ans + (i - start + 1) * (i - start) // 2) % MOD

        return ans