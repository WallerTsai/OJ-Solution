class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1_000:
            return 0
        
        ans = 0
        while n >= 1_000:
            ans += n - 1_000 + 1
            n %= 1_000
        return ans  # 错误
    
class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1_000:
            return 0
        
        ans = 0
        cur = 1_000
        while n >= cur:
            ans += n - cur + 1
            cur *= 1_000
        return ans

print(Solution().countCommas(1_002))
print(Solution().countCommas(1004590))


