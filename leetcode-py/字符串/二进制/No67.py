# class Solution:
#     #内置函数法
#     def addBinary(self, a: str, b: str) -> str:
#         # int(s,base=2) 以二进制形式转换成十进制整数
#         bin_a = int(a,base=2)
#         bin_b = int(b,base=2)
#         res = bin(bin_a + bin_b)[2:]
#         return res

class Solution:
    # 非内置函数法
    def addBinary(self, a: str, b: str) -> str:

        #用"0"补齐位置
        differ = len(a) - len(b)
        if differ >= 0:
            b = '0' * differ + b
        else:
            a = '0' * -differ + a

        res = ""
        temp = 0
        # 巧用zip()
        for i,j in zip(a[::-1],b[::-1]):
            s = int(i) + int(j) + temp
            res = str(s%2) + res
            temp = s // 2

        # 处理后续
        if temp:
            res = '1' + res
        
        return res
    
if __name__ == "__main__":
    fun = Solution()
    a ="1"
    b = "111"
    res = fun.addBinary(a,b)