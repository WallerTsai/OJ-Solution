from math import ceil


class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        l = 2 * k + 1
        n = (n + 1) // l
        m = (m + 1) // l
        return n * m if n and m else 1
    
class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        l = 2 * k + 1
        n = ceil(n / l)
        m = ceil(m / l)
        return n * m 