# 预处理因子
MX = 100_001
divisor_num = [0] * MX
divisor_sum = [0] * MX
for i in range(1, MX):
    for j in range(i, MX, i):  # 枚举 i 的倍数 j
        divisor_num[j] += 1  # i 是 j 的因子
        divisor_sum[j] += i

