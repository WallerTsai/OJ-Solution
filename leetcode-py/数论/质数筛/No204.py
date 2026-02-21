from math import isqrt

class Solution:
    def countPrimes(self, n: int) -> int:
        def is_Prime(num:int)->bool:
            if num < 2:
                return False
            for i in range(2,isqrt(num)+1):
                if num % i == 0:
                    return False
            return True
        res = 0
        for i in range(1,n):
            if is_Prime(i):
                res += 1
        return res  #超时
    
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        if n == 2:
            return 1
        def is_Prime(num:int)->bool:
            if num < 2:
                return False
            for i in range(2,isqrt(num)+1):
                if num % i == 0:
                    return False
            return True
        res = 0
        for i in range(1,n,2):
            if i > 10 and str(i)[-1] == '5':
                continue
            if is_Prime(i):
                res += 1
        return res  #超时
    
class Solution:
    #厄拉多塞筛法
    def countPrimes(self, n: int) -> int:
        isPrimes = [1] * n
        res = 0
        for i in range(2, n):
            if isPrimes[i] == 1: res += 1
            j = i
            while i * j < n:
                isPrimes[i * j] = 0
                j += 1
        return res  #差一点
    
class Solution:
# 作者：powcai
    def countPrimes(self, n: int) -> int:
        if n < 2: 
            return 0
        
        isPrimes = [1] * n
        isPrimes[0] = isPrimes[1] = 0
        for i in range(2, isqrt(n)+1):
            if isPrimes[i] == 1:
                # 这个切片绝了
                isPrimes[i * i: n: i] = [0] * len(isPrimes[i * i: n: i])
        return sum(isPrimes)    # 886ms

