class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()
    
class Solution:
    def hammingWeight(self, n: int) -> int:
        # 每次执行 n &= n - 1，n 的二进制表示中最右边的 1 会被变成 0，直到 n 变为 0。
        # 通过计数这个操作执行的次数，可以得到 n 的二进制表示中 1 的个数。
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res