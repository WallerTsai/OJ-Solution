class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        ans = 0
        MOD = 10 ** 9 + 7
        n = r - l + 1
        m = (((pow(10, k, MOD) - 1)) * pow(9, -1, MOD)) % MOD
        for i in range(l, r + 1):
            t = (i * pow(n, k - 1, MOD)) % MOD
            ans = (ans + t * m) % MOD
        return ans
            