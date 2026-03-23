from functools import cache


class Solution:
    def almostPalindromic(self, s: str) -> int:
        @cache
        def check(t):
            m = len(t)
            left = 0
            right = m - 1
            while left < right and t[left] == t[right]:
                left += 1
                right -= 1

            s1 = t[left + 1: right + 1]
            if s1 == s1[::-1]:
                return True
            s2 = t[left: right - 1 + 1]
            if s2 == s2[::-1]:
                return True
            return False
        
        n = len(s)
        for k in range(n, 1, -1):
            for i in range(0, n - k + 1):
                t = s[i: i + k]
                if check(t):
                    return k
            check.cache_clear()
        return 1    # 错误
    
# 看到回文串应该先想到中心扩展法和马拉车算法
class Solution:
    # 中心扩展法
    def almostPalindromic(self, s: str) -> int:
        n = len(s)
        ans = 0

        def func(l: int, r: int):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        
        for i in range(2 * n - 1):  # 妙
            l, r = i // 2, (i + 1) // 2
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            ans = max(ans, func(l - 1, r), func(l, r + 1))
            if ans >= n:
                return n
        return ans


Solution().almostPalindromic("aab")
