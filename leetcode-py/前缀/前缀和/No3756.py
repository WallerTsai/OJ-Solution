from typing import List

MOD = pow(10, 9) + 7
pow10 = [1] * (10 ** 5 + 1)
for i in range(1, 10 ** 5 + 1):
    pow10[i] = (pow10[i - 1] * 10) % MOD
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        li = list(map(int, s))
        n = len(li)

        pre_sum = [0] * (n + 1)
        pre_digit = [0] * (n + 1)
        pre_length = [0] * (n + 1)
        for i, num in enumerate(li):
            pre_sum[i + 1] = pre_sum[i] + num
            pre_digit[i + 1] = (pre_digit[i] * 10 + num) % MOD if num else pre_digit[i]
            pre_length[i + 1] = pre_length[i] + 1 if num else pre_length[i]

        res = []
        for l, r in queries:
            length = pre_length[r + 1] - pre_length[l]
            if length == 0:
                res.append(0)
                continue

            total = pre_sum[r + 1] - pre_sum[l]
            x = (pre_digit[r + 1] - pre_digit[l] * pow10[length] + MOD) % MOD
            ans = (x * total) % MOD
            res.append(ans)

        return res

# 注意要中途进行取模, 大数运算太浪费时间
