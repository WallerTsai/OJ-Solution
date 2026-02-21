from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        aset1 = set()
        aset2 = set()
        for x in nums:
            if x in aset2:
                continue
            elif x in aset1:
                aset1.discard(x)
                aset2.add(x)
            else:
                aset1.add(x)
        return aset1.pop()
    
class Solution:
    # 灵神
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(31):
            cnt1 = sum(x >> i & 1 for x in nums)
            ans |= cnt1 % 3 << i
        # 最高位是符号位，下面这行相当于统计负数的个数
        cnt1 = sum(x >> 31 & 1 for x in nums)
        # 如果 cnt1 % 3 == 1，那么答案的最高位是 1，否则是 0
        # Python 只能通过减法把最高位置为 1
        return ans - (cnt1 % 3 << 31)   # 32ms
        return -ans if (cnt1 % 3 << 31) else ans    #错误



# 测试
print(5 >> 31)      # 0（正数右移补0）
print(-5 >> 31)     # -1（负数右移补1）

# 但取最后一位
print(5 >> 31 & 1)   # 0
print(-5 >> 31 & 1)  # 1

# Python vs C 的存储对比
# 数字	    C语言（32位补码）	                      Python  （符号-数值）（某种结构）
#  5	    00000000 00000000 00000000 00000101	    符号: +, 数值: 5
# -5	    11111111 11111111 11111111 11111011	    符号: -, 数值: 5
# -1	    11111111 11111111 11111111 11111111	    符号: -, 数值: 1

# 如果不这么做的话测试用例是[-2,-2,1,1,-3,1,-3,-3,-4,-2] 的时候，就会输出 4294967292。 
# 其原因在于Python是动态类型语言，在这种情况下其会将符号位置的1看成了值，而不是当作符号“负数”。 
# 这是不对的。 正确答案应该是 - 4，-4的二进制码是 1111...100，就变成 2^32-4=4294967292，
# 解决办法就是 减去 2 ** 32 。

# python中 4294967292 = 11111111 11111111 11111111 11111100
# 别的语言          -4 = 11111111 11111111 11111111 11111100


class Solution:
    # 灵神
    # 模3运算
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for x in nums:
            a, b = (a ^ x) & (a | b), (b ^ x) & ~a
        return b    # 3ms
    
class Solution:
    # 灵神
    # 模3运算
    # https://leetcode.cn/problems/single-number-ii/
    # 注意题解中：由于位运算具有「并行计算」的特点，上述运算规则可以推广到多个比特的情况。
    def singleNumber(self, nums: List[int]) -> int:
        # (0,0)→(0,1)→(1,0)
        a = b = 0
        for x in nums:
            b = (b ^ x) & ~a
            a = (a ^ x) & ~b
        return b
        # 这里模拟一遍理解 

fun = Solution()
fun.singleNumber([2,2,3,2])