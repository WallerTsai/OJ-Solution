class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s, m = 0, 1
        x = n
        while x:
            x, d = divmod(x, 10)
            s += d
            m *= d
        return n % (s + m) == 0