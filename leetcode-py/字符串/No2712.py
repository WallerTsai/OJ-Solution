class Solution:
    def minimumCost(self, s: str) -> int:
        ans = 0
        n = len(s)

        if n == 1:
            return 0

        # 左边
        for i in range(1,n // 2 + 1):
            if s[i] != s[i - 1]:
                ans += i

        # 右边
        for j in range(n - 2,n // 2 - 1,-1):
            if s[j] != s[j + 1]:
                ans += n - j -1
        
        return ans

class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(1,n):
            if s[i] != s[i - 1]:
                ans += min(i,n - i)
        return ans