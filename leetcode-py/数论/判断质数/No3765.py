from functools import cache
from math import isqrt


class Solution:
    def is_Prime(self,num:int)->bool:
            if num < 2:
                return False
            for i in range(2,isqrt(num)+1):
                if num % i == 0:
                    return False
            return True
    
    def completePrime(self, num: int) -> bool:
        
        s = str(num)
        n = len(s)
        for i in range(n):
            if not self.is_Prime(int(s[i:])):
                 return False
            if not self.is_Prime(int(s[:i + 1])):
                 return False
        return True
    

class Solution:
    
    def completePrime(self, num: int) -> bool:
        s = str(num)
        @cache
        def is_Prime(num:int)->bool:
            if num < 2:
                return False
            for i in range(2,isqrt(num)+1):
                if num % i == 0:
                    return False
            return True
        
        @cache
        def bt(t: str):
            if not is_Prime(int(t)):
                return False
        
            if len(t) == 1:
                return True
            
            return  bt(t[1:]) and bt(t[:-1])
            
        return bt(s)    # 错误
    
class Solution:
    def completePrime(self, num: int) -> bool:

        @cache
        def is_Prime(num:int)->bool:
            if num < 2:
                return False
            for i in range(2,isqrt(num)+1):
                if num % i == 0:
                    return False
            return True
        
        s = str(num)
        n = len(s)
        for i in range(n):
            if not is_Prime(int(s[i:])):
                 return False
            if not is_Prime(int(s[:i + 1])):
                 return False
        return True
 
    
def is_prime(n: int) -> bool:
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n >= 2  # 1 不是质数

class Solution:
    # 灵神
    def completePrime(self, num: int) -> bool:
        s = str(num)
        for i in range(len(s)):
            # 前缀
            x = int(s[:i + 1])
            if not is_prime(x):
                return False

            # 后缀
            x = int(s[i:])
            if not is_prime(x):
                return False

        return True