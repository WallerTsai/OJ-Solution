from math import comb

# https://leetcode.cn/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/solutions/3033292/
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 1_000_000_007
        return comb(n - 1, k) % MOD * m * pow(m - 1, n - k - 1, MOD) % MOD
    
MOD = 10**9 + 7


# 大佬模板

# 快速幂求模逆元
def mod_inverse(x):
    return pow(x, MOD - 2, MOD)

# 预处理阶乘与逆元
def precompute_factorials(limit):
    fact = [1] * (limit + 1)
    for i in range(1, limit + 1):
        fact[i] = fact[i - 1] * i % MOD
    # 逆元
    inv_fact = [1] * (limit + 1)
    inv_fact[limit] = mod_inverse(fact[limit])
    for i in range(limit - 1, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    return fact, inv_fact

# 组合数函数
def comb(n, k):
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

# 一次性预处理
MAX_N = 10**5
fact, inv_fact = precompute_factorials(MAX_N)

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return comb(n - 1, k) * m * pow(m - 1, n - k - 1, MOD) % MOD