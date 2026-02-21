#这里介绍快速幂方法,实现 O(logn) 时间复杂度

class Solution:
    def myPow(self, x: float, n: int) -> float:

        if x == 0:
            return 0.0
        
        res = 1

        if n < 0:
            x,n = 1/x,-n
        while n:
            if n & 1:
                res *= x
            x *=x
            n >>= 1

        return res

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def f(x,n):
            if n == 1:
                return x
            if n == 0:
                return 1
            tmp = f(x, n//2)
            if n % 2 == 1:
                return tmp*tmp*x
            else:
                return tmp*tmp
        if n==0:
            return 1
        if n<0:
            return 1/f(x,-n)
        return f(x,n)
