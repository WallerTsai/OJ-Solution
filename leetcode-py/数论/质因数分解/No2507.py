class Solution:
    def smallestValue(self, n: int) -> int:
        flag = True
        while flag:
            if n == 4:
                return 4
            flag = False
            next_n, copy_n = 0, n
            i = 2
            while i ** 2 <= copy_n:
                while copy_n % i == 0:
                    next_n += i
                    flag = True
                    copy_n //= i
                i += 1
            if 1 < copy_n < n:
                next_n += copy_n
            elif copy_n == n:
                return n
            n = next_n


class Solution:
    def smallestValue(self, n: int) -> int:
        while True:
            x, s, i = n, 0, 2
            while i * i <= x:
                while x % i == 0:
                    s += i
                    x //= i
                i += 1
            if x > 1: s += x
            if s == n: return n
            n = s