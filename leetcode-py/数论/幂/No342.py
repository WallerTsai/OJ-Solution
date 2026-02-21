class Solution:
    # 递归
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 1:
            return True
        elif n % 4 != 0:
            return False
        else:
            return self.isPowerOfFour(n // 4)
        
class Solution:
    # leetcode大佬
    def isPowerOfFour(self, n: int) -> bool:
        # 二进制中的1只有一个，并且0的个数是2的倍数
        # 这里因为二进制是0bxxx所以0的个数会多一个标志0,所以0的个数必须是奇数
        return bin(n).count('1') == 1 and bin(n).count('0') % 2 == 1 if n > 0 else False

class Solution:
    # 利用特性
    def isPowerOfFour(self, n: int) -> bool:
        # 判断 n 是否是 2 的幂
        if n & (n - 1) != 0:
            return False
        
        # 判断 n 除以 3 的余数是否为 1
        if n % 3 != 1:
            return False
        
        return True
    
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and n & 0x55555555 > 0