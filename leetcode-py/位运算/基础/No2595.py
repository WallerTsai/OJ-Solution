from typing import List
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        if n == 1:
            return [1,0]
        s = bin(n)[-1:1:-1]
        even = s[::2].count('1')
        odd = s[1::2].count('1')
        return [even,odd]   # 0ms

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        res = [0,0]
        index = 0
        while n:
            res[index] += n & 1
            n >>= 1
            index = (index+1) % 2
        return res  # 0 - 4ms


# 利用位掩码 0x55555555（二进制的 010101⋯），取出偶数下标比特和奇数下标比特，
# 分别用库函数统计 1 的个数。
# 本题由于 n 范围比较小，取 0x5555 作为位掩码。
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        MASK = 0x5555
        return [(n & MASK).bit_count(), (n & (MASK >> 1)).bit_count()]


