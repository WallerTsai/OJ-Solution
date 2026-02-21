from math import gcd


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = sumEven = 0
        for i in range(1, 2 * n):
            if i % 2:
                sumOdd += i
            else:
                sumEven += i
        return gcd(sumOdd, sumEven)
    
class Solution:
    # 可以证明
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n