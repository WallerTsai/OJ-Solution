class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        n = 1
        i = 2
        while i ** 2 < num:
            if num % i == 0:
                n += i + num//i
            i += 1
        if i > 1 and i ** 2 == num:
            n += i
        return n == num