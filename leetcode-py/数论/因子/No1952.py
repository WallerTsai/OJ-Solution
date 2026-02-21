from math import isqrt, sqrt


class Solution:
    # 暴力
    def isThree(self, n: int) -> bool:
        count = 0
        if n <= 3: return False
        for i in range(2,n):
            if n % i == 0:
                count += 1
                if count > 1:
                    return False
        return count == 1   # 4ms
    
# 这道题本质是判断是不是一个完全平方数，且平方根必须是质数,除了1，平方根和本身再无别的因素
# 对于数n，如果d是n的一个除数，那么n/d 也是n的一个除数

class Solution:
    def isThree(self, n: int) -> bool:
        cnt = 0
        x = 1
        while x * x <= n:
            if n % x == 0:
                cnt += 1
                if x * x != n:
                    cnt += 1
            x += 1
        return cnt == 3

# 其实证明n开方得到的数是质数，则n也没有处1和本身以外的除数
class Solution:
    def isThree(self, n: int) -> bool:
        def isPrime(x):
            for i in range(2, int(sqrt(x)) + 1):
                if x % i == 0:
                    return False
            return True if x > 1 else False

        p = int(sqrt(n))
        return p * p == n and isPrime(p)
