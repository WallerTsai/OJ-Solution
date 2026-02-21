class Solution:
    def sumOfMultiples(self, n: int) -> int:
        aset = set()
        f3 = 3
        f5 = 5
        f7 = 7
        while f3 <= n:
            aset.add(f3)
            f3 += 3
        while f5 <= n:
            aset.add(f5)
            f5 += 5
        while f7 <= n:
            aset.add(f7)
            f7 += 7
        return sum(aset)    # 19ms
    
class Solution:
    # 容斥原理
    def sumOfMultiples(self, n: int) -> int:
        def s(m: int) -> int:
            k = n // m
            return k * (k + 1) // 2 * m
        return s(3) + s(5) + s(7) - s(15) - s(21) - s(35) + s(105)  # 0ms