from itertools import accumulate


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        pass



class Solution:
    # 灵神
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1_000_000_007
        k = r - l + 1

        f0 = [1] * k  # 后两个数递增
        f1 = [1] * k  # 后两个数递减
        for _ in range(n - 1):
            s0 = list(accumulate(f0, initial=0))
            s1 = list(accumulate(f1, initial=0))
            for j in range(k):
                f0[j] = s1[j] % MOD
                f1[j] = (s0[k] - s0[j + 1]) % MOD

        return (sum(f0) + sum(f1)) % MOD