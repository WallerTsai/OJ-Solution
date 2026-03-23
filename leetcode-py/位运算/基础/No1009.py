class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        # 找到 n 的最高位
        highest_bit = 0
        temp = n
        while temp > 0:
            highest_bit += 1
            temp >>= 1
        
        # 创建一个所有位都是 1 的掩码
        mask = (1 << highest_bit) - 1
        
        # 使用掩码与 n 进行异或操作
        return n ^ mask
    
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        # 计算 n 的位数
        bit_length = n.bit_length()
        
        # 生成一个与 n 位数相同的全 1 掩码
        mask = (1 << bit_length) - 1
        
        # 使用掩码与 n 进行异或操作
        return n ^ mask
    

# 2026年3月11日
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            # zero = 0
            # print(zero.bit_length())
            # >>> 0
            return 1
        
        m = n.bit_length()
        return ((1 << m) - 1) ^ n
    

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return ~n   # 错误
