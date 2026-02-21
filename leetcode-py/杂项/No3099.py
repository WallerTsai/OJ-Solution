class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = 0
        t = x
        while t:
            t, d = divmod(t, 10)
            s += d
        return s if x % s == 0 else -1


