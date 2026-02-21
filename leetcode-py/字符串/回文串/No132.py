from functools import cache
from math import inf


class Solution:
    def minCut(self, s: str) -> int:
        @cache
        def isPalindrome(l:int, r:int) -> bool:
            if l >= r:
                return True
            return s[l:r+1] == s[r:l-1:-1]
        @cache
        def dfs(r: int) -> int:
            if s[:r+1] == s[r::-1]:
                return 0
            ans = inf
            for l in range(1,r+1):
                if isPalindrome(l,r):
                    ans = min(ans,dfs(l-1) + 1)
            return ans
    
        return dfs(len(s) - 1)  # 2930ms
    
# 注意判断回文串的方法
class Solution:
    # 灵神
    def minCut(self, s: str) -> int:
        # 返回 s[l:r+1] 是否为回文串
        @cache  # 缓存装饰器，避免重复计算 is_palindrome（一行代码实现记忆化）
        def is_palindrome(l: int, r: int) -> bool:
            if l >= r:
                return True
            return s[l] == s[r] and is_palindrome(l + 1, r - 1)

        @cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(r: int) -> int:
            if is_palindrome(0, r):  # 已是回文串，无需分割
                return 0
            res = inf
            for l in range(1, r + 1):  # 枚举分割位置
                if is_palindrome(l, r):
                    res = min(res, dfs(l - 1) + 1)  # 在 l-1 和 l 之间切一刀
            return res

        return dfs(len(s) - 1)

fun = Solution()
fun.minCut("aab")