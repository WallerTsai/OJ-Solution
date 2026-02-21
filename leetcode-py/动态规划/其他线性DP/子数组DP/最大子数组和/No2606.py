from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        map = dict()
        map.update(zip(chars, vals))

        def f(i: int):
            if s[i] not in chars:
                return ord(s[i]) - ord('a') + 1
            return map[s[i]]
        
        n = len(s)
        dp = [0] * n
        dp[0] = f(0)

        for i in range(1,n):
            dp[i] = max(dp[i - 1], 0) + f(i)

        return max(0,*dp)   # 223ms
    
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        mapping = dict(zip(chars, vals))
        ans = f = 0
        for c in s:
            f = max(f, 0) + mapping.get(c, ord(c) - ord('a') + 1)
            ans = max(ans, f)
        return ans  # 202ms