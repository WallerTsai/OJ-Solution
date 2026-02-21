class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            while n % 3 == 0:
                n //= 3
            else:
                n -= 1
            if n % 3:
                return False
        return True
    
class Solution:
    # 三进制
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n % 3 == 2:
                return False
            n //= 3
        return True
    