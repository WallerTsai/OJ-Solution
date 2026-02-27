class Solution:
    # 每次添加一个数就相当于将前面的数向左位移，然后加上新数
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        ans = 0
        for i in range(1, n + 1):
            ans = ((ans << i.bit_length()) + i) % MOD
        return ans



