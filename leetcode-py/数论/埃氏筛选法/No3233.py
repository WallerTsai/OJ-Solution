
from math import isqrt

# copy by 灵神
# 没想出来

# 1. 只有质数的平方才是特殊数字
# 2. 区间[0, i] 中特殊数字个数 等于[0,isqrt(i)]中质数数量

# 预处理质数数量统计
MX = isqrt(10 ** 9)
pi = [0] * (MX + 1)
for i in range(2, MX + 1):
    if pi[i] == 0:  # i 是质数
        pi[i] = pi[i - 1] + 1
        for j in range(i * i, MX + 1, i):
            pi[j] = -1  # 标记 i 的倍数为合数
    else:
        pi[i] = pi[i - 1]

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        return r - l + 1 - (pi[isqrt(r)] - pi[isqrt(l - 1)])

