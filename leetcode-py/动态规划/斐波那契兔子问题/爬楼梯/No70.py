# class Solution:
#     def __init__(self) -> None:
#         self.counter = 0
#     def climbStairs(self, n: int,flat:int = 1) -> int:
#         if n == 0:
#             self.counter += 1
#             return
#         if n >= 2:
#             self.climbStairs(n-2,flat=0)
#         self.climbStairs(n-1,flat=0)
#         if flat == 1:
#             return self.counter
#     # 太慢了


from functools import cache


class Solution:
    def __init__(self) -> None:
        self.cache = {}
    def climbStairs(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        self.cache[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
        return self.cache[n]

class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        res = self.climbStairs(n-2) + self.climbStairs(n-1)

        return res

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        cache = [0] * n
        cache[0] = 1
        cache[1] = 2
        for i in range(2,n):
            cache[i] = cache[i-2] + cache[i-1]

        return cache[n-1]

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        n0 = 1
        n1 = 2
        res = 0
        for _ in range(2,n):
            res = n1 + n0
            n0,n1 = n1,res

        return res


fun = Solution()
print(fun.climbStairs(n = 38))