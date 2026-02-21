# 计算位数：

# 使用 n.bit_length() 获取 n 的二进制表示的位数。例如，对于 n = 5，其二进制表示是 101，位数为 3。
# 左移操作：

# 使用 1 << bit_length 将 1 左移 bit_length 位。例如，对于 bit_length = 3，1 << 3 的结果是 1000（二进制表示为 8）。
# 减 1 操作：

# 从左移后的结果中减去 1，得到一个与 n 位数相同的全 1 掩码。例如，8 - 1 的结果是 7，其二进制表示为 111。

class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        
        bit_length = num.bit_length()

        # 生成一个与num位数相同的全 1 掩码
        mask = ( 1 << bit_length) - 1

        return num ^ mask

