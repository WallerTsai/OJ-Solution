class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:][::-1], 2) # 错误，位置丢失
    
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans << 1) | (n & 1)
            n >>= 1
        return ans  # 38ms

class Solution:
    # 分治
    def reverseBits(self, n: int) -> int:
        # 交换 16 位
        n = ((n >> 16) | (n << 16)) & 0xFFFFFFFF
        # 交换每个 8 位块
        n = (((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)) & 0xFFFFFFFF
        # 交换每个 4 位块
        n = (((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)) & 0xFFFFFFFF
        # 交换每个 2 位块
        n = (((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)) & 0xFFFFFFFF
        # 交换相邻位
        n = (((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)) & 0xFFFFFFFF
        return n
    

def hex32_bin(x: int) -> str:
    """把 16 进制整数（如 0x1a3f）转成 32 位固宽二进制字符串"""
    return format(x, '032b')

print(hex32_bin(0xFF00FF00))
print(hex32_bin(0x00FF00FF))

print(hex32_bin(0xF0F0F0F0))
print(hex32_bin(0x0F0F0F0F))

print(hex32_bin(0xCCCCCCCC))
print(hex32_bin(0x33333333))

print(hex32_bin(0xAAAAAAAA))
print(hex32_bin(0x55555555))


class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)
    

class Solution:
    def dec32_bin(self,x: int) -> str:
        """把十进制整数转换成32位固宽二进制字符串"""
        return format(x, '032b')

    def reverseBits(self, n: int) -> int:
        return int(self.dec32_bin(n)[::-1], 2)