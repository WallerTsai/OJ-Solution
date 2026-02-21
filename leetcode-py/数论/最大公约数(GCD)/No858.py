import math

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        gcd = math.gcd(p,q)
        p = (p // gcd) % 2
        q = (q // gcd) % 2

        if p and q: return 1
        if p == 0: return 2
        return 0