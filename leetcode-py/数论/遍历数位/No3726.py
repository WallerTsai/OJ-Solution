class Solution:
    def removeZeros(self, n: int) -> int:
        return int(str(n).replace('0', ''))
    
class Solution:
    def removeZeros(self, n: int) -> int:
        return int(''.join(i for i in str(n) if i>'0'))

        

class Solution:
    def removeZeros(self, n: int) -> int:
        ans = 0
        pow10 = 1
        while n:
            n, d = divmod(n, 10)
            if d > 0:
                ans += d * pow10
                pow10 *= 10
        return ans