MOD = 10 ** 9 + 7

class Solution:
    # 正难则反
    def monkeyMove(self, n: int) -> int:
        return (pow(2, n, MOD) - 2) % MOD