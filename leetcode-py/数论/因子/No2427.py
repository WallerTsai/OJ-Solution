# 暴力也可以解

from math import gcd


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        g = gcd(a,b) # 最大公约数
        ans, i = 0, 1
        # 枚举到最大公约数的开方
        while i * i <= g:
            if g % i == 0:
                ans += 1 # i 是公因子
                if i * i < g:
                    ans += 1 # g/i 是公因子
            i += 1
        return ans 
    
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        g = gcd(a,b) # 最大公约数
        ans, i = 0, 1
        # 枚举到最大公约数的开方
        while i * i <= g:
            if g % i == 0:
                ans += 1 # i 是公因子
                if i * i != g:
                    ans += 1 # g/i 是公因子
            i += 1
        return ans 