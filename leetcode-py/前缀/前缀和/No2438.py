from itertools import accumulate
from typing import List

# 综合运用

# 找规律
# n = 2 时, 其二进制为 10 , 对应的 powers = [2]
# n = 15 时, 其二进制为 1111, 对应 powers = [1, 2, 4, 8]

# 同时 powers 里面没有相同元素 假设存在 4 4 这会合成 8

# 利用 底数相同, 两数相乘等价于同底指数相加，构造前缀和
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        exps = []
        bit = 0
        while n:
            if n & 1 == 1:
                exps.append(bit)
            n >>= 1
            bit += 1
        
        pre_sum  = list(accumulate(exps, initial = 0))

        ans = []
        for l, r in queries:
            total_exps = pre_sum[r + 1] - pre_sum[l]
            pow2 = pow(2, total_exps)
            ans.append(pow2 % MOD)

        return ans  # 95ms
    
MOD = 1_000_000_007
MX = 436
pow2 = [0] * MX
pow2[0] = 1

# 预处理 2^i % MOD
for i in range(1, MX):
    pow2[i] = pow2[i - 1] * 2 % MOD

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        prefix = [0]  # 指数前缀和数组
        while n:
            lowbit = n & -n
            e = lowbit.bit_length() - 1     # 求指数 e
            prefix.append(prefix[-1] + e)   # 指数累加
            n ^= lowbit                     # 去掉最低位 1
        
        # 查询
        return [pow2[prefix[r + 1] - prefix[l]] for l, r in queries]    # 23ms