from bisect import bisect_left
from math import isqrt
class Solution:
        
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
    
    def is_Prime(self,num:int)->bool:
            if num < 2:
                return False
            for i in range(2,isqrt(num)+1):
                if num % i == 0:
                    return False
            return True
    def primePalindrome(self, n: int) -> int:
        NEXT_HEAD = {'2':3, '4':7, '5':7, '6':7, '8':9}

        if n <= 2:
            return 2
        
        res = n

        while True:
            s = str(res)
            length = len(s)

            # 除了11以外，所有偶数长度的回文数都不是素数(自行证明)、
            if length % 2 == 0 and length > 2:
                res = 10 ** length  #升位处理
                continue

            # 大于10的数中，结尾是2，4，5，6，8都不是素数(没有0，因为回文数没有0开头)
            if length>2 and s[0] in '24568':
                res = NEXT_HEAD[s[0]] * 10 ** (length - 1)
                continue

            # 判断回文
            if not self.isPalindrome(res):
                res += 1
                continue

            # 判断素数
            if not self.is_Prime(res):
                res += 1
                continue
            else:
                break

        return res


# 以下是leetcode最快    
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def cal(i):
    # 奇数位
    for x in range(10 ** (i - 1), 10 ** i):
        cur = int(str(x) + str(x)[:-1][::-1])
        yield cur
    if i==1:
        # 偶数位
        for x in range(10 ** (i - 1), 10 ** i):
            cur = int(str(x) + str(x)[::-1])
            yield cur
t = []
for i in range(1,6):
    for x in cal(i):
        if is_prime(x):
            t.append(x)

class Solution:
    def primePalindrome(self,n:int):
        return t[bisect_left(t,n)]
