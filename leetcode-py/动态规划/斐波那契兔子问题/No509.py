class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for i in range(n - 1):
            b, a = a + b, b
        return b
    
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        n1, n2 = 0, 1
        for _ in range(2, n + 1):
            n2, n1 = n1 + n2, n2
        return n2