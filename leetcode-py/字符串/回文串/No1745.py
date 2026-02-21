from functools import cache
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        @cache
        def ispalindrome(l: int, r: int) -> int:
            if l >= r:
                return True
            if s[l] == s[r] and ispalindrome(l+1,r-1):
                return True
            else:
                return False
            
        @cache
        def dfs(index:int,k:int) -> int:
            if k == 0:
                return ispalindrome(0,index)
            for l in range(k,index+1):
                if ispalindrome(l,index) and dfs(l-1,k-1):
                    return True 
            return False

        return dfs(len(s)-1,3-1)    # 1519ms

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        @cache
        def ispalindrome(l: int, r: int) -> int:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
            
        @cache
        def dfs(index:int,k:int) -> int:
            if k == 0:
                return ispalindrome(0,index)
            for l in range(k,index+1):
                if ispalindrome(l,index) and dfs(l-1,k-1):
                    return True 
            return False

        return dfs(len(s)-1,3-1)    # 超时
    

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)

        ispalindrome = [[True] * n for _ in range(n)]
        for l in range(n-2,-1,-1):
            for r in range(l+1,n):
                if s[l] != s[r] or ispalindrome[l+1][r-1] is False:
                    ispalindrome[l][r] = False

            
        @cache
        def dfs(index:int,k:int) -> int:
            if k == 0:
                return ispalindrome[0][index]
            for l in range(k,index+1):
                if ispalindrome[l][index] and dfs(l-1,k-1):
                    return True 
            return False

        return dfs(len(s)-1,3-1) # 1613ms

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)

        ispalindrome = [[True] * n for _ in range(n)]
        for l in range(n-2,-1,-1):
            for r in range(l+1,n):
                if s[l] != s[r] or ispalindrome[l+1][r-1] is False:
                    ispalindrome[l][r] = False

        # 枚举两个分割处
        for i in range(n-2):
            for j in range(i+1,n-1):
                if ispalindrome[0][i] and ispalindrome[i+1][j] and ispalindrome[j+1][-1]:
                    return True
        return False