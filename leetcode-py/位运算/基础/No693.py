class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        temp = n >> 1
        xro = n ^ temp
        mask = (1 << n.bit_length()) - 1
        if not (xro ^ mask):
            return True
        return False
    
class Solution:
    # 如何快速判断全部为是1？其实就是判断是否异或结果为2的幂次减一。
    # 判断2的幂次a的位运算方法为a&(a+1)==0
    def hasAlternatingBits(self, n: int) -> bool:
        return not (a := n ^ (n >> 1)) & (a + 1)
