class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5
        return (5 ** ((n + 1)// 2) * 4 ** (n // 2)) % (10 ** 9 + 7) # 超时
    
#快速幂函数
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 1_000_000_007
        return pow(5, (n + 1) // 2, MOD) * pow(4, n // 2, MOD) % MOD