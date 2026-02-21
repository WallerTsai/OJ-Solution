# class Solution:
#     def countBinaryPalindromes(self, n: int) -> int:
#         if n == 0:
#             return 1
#         if n == 1:
#             return 2
        
#         bit_l = n.bit_length()
#         ans = 2

#         for l in range(2, bit_l):
#             ans += 1 << ((l - 1) // 2)

#         start = 1 << ((bit_l + 1) // 2 - 1)
#         end = 1 << (bit_l + 1) // 2
#         for i in range(start, end):
#             half_s = bin(i)[2:]
#             if bit_l % 2:
#                 s = half_s + half_s[::-1]
#             else:
#                 s = half_s + half_s[-2::-1]

#             num = int(s, 2)

#             if num <= n:
#                 ans += 1
#             else:
#                 break

#         return ans
    

# class Solution:
#     def countBinaryPalindromes(self, n: int) -> int:
#         if n == 0:
#             return 1
#         if n == 1:
#             return 2
        
#         bit_l = n.bit_length()
#         ans = 2

#         for l in range(2, bit_l):
#             ans += 1 << ((l - 1) // 2)
            
#         start = 1 << ((bit_l + 1) // 2 - 1)
#         end = 1 << (bit_l + 1) // 2
#         for i in range(start, end):
#             half_s = bin(i)[2:]
#             if bit_l % 2 == 0:
#                 s = half_s + half_s[::-1]
#             else:
#                 s = half_s + half_s[-2::-1]

#             num = int(s, 2)
#             if num <= n:
#                 ans += 1
#             else:
#                 break

#         return ans
    
# class Solution:
#     def countBinaryPalindromes(self, n: int) -> int:
#         if n == 0:
#             return 1
#         if n == 1:
#             return 2

#         bit_l = n.bit_length()
#         ans = 2 

#         for l in range(2, bit_l):
#             ans += 1 << ((l - 1) // 2)

#         half_len = (bit_l + 1) // 2
#         start = 1 << (half_len - 1)
#         end = 1 << half_len

#         for i in range(start, end):
#             tail = i >> (1 if bit_l % 2 else 0)
#             reversed = 0
#             tmp = tail
#             for _ in range(bit_l - half_len):
#                 reversed = (reversed << 1) | (tmp & 1)
#                 tmp >>= 1
#             num = (i << (bit_l - half_len)) | reversed

#             if num <= n:
#                 ans += 1
#             else:
#                 break

#         return ans

# import bisect

# print(1)
# cnt = [0, 1]
# for L in range(2, 51): 
#     half = (L + 1) // 2
#     base = 1 << (half - 1)
#     end  = 1 << half
#     for prefix in range(base, end):
#         suffix = prefix >> (1 if L % 2 else 0)
#         rev = 0
#         tmp = suffix
#         for _ in range(L - half):
#             rev = (rev << 1) | (tmp & 1)
#             tmp >>= 1
#         pal = (prefix << (L - half)) | rev
#         cnt.append(pal)
# cnt.sort()

# class Solution:
#     def countBinaryPalindromes(self, n: int) -> int:
#         return bisect.bisect_right(cnt, n)
    


# 上面都超时


# 题目：统计二进制回文数字的数目

# 正解
from math import ceil


def binsearch(ub, mid):
    l = 0
    r = 10**8
    while l <= r:
        m = (l + r) >> 1
        left = bin(m)[2:]
        right = left[::-1]
        num = int(left + mid + right, 2)
        if num <= ub:
            l = m + 1
        else:
            r = m - 1
    return r + 1

class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        if n <= 1:
            return n + 1
        return binsearch(n, '') + binsearch(n, '0') + binsearch(n, '1') - 1
    

class Solution1:
    def countBinaryPalindromes(self, n: int) -> int:
        if n == 0:
            return 1

        m = n.bit_length()  # n 的二进制长度

        # 二进制长度小于 m，随便填
        ans = 1  # 0 也是回文数
        # 枚举二进制长度，最高位填 1，回文数左半的其余位置随便填
        for i in range(1, m):
            ans += 1 << ((i - 1) // 2)

        # 最高位一定是 1，从次高位开始填
        for i in range(m - 2, m // 2 - 1, -1):
            if n >> i & 1:
                # 这一位可以填 0，那么回文数左半的剩余位置可以随便填
                ans += 1 << (i - m // 2)
            # 在后续循环中，这一位填 1

        pal = n >> (m // 2)
        # 左半反转到右半
        # 如果 m 是奇数，那么去掉回文中心再反转
        v = pal >> (m % 2)
        while v:
            pal = pal * 2 + v % 2
            v //= 2
        if pal <= n:
            ans += 1

        return ans

    
class Solution2:
    def countBinaryPalindromes(self, n: int) -> int:
        # 如果 n 为 0，只有一个回文数 0
        if n == 0:
            return 1

        mx_l = len(bin(n)) - 2  # n 的二进制长度
        ans = 1  # 包含 0

        # 枚举长度小于 mx_l 的所有二进制回文数
        for l in range(1, mx_l):
            half_len = ceil(l / 2)  # 回文数的一半长度
            ans += (1 << (half_len - 1))  # 该长度的回文数个数

        half_len = ceil(mx_l / 2)
        mn = 1 << (half_len - 1)  # 最小的半部分
        pre = int(bin(n)[2:][:half_len], 2)  # n 的前半部分
        ans += (pre - mn)  # 加上前半部分在范围内的回文数       # 这里很妙，没有包含 "pre"

        s = bin(pre)[2:]  # 前半部分的二进制字符串
        # 拼接成回文串
        if mx_l % 2 == 0:
            temp = s + s[::-1]
        else:
            temp = s + s[:-1][::-1]

        # 判断拼接后的回文数是否小于等于 n
        return ans + 1 if int(temp, 2) <= n else ans    # 0ms
    
fun1 = Solution1()
fun2 = Solution2()
n = 0b111000   # 1 后面 43 个 0
print(fun1.countBinaryPalindromes(n), fun2.countBinaryPalindromes(n))

class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 2
        
        bit_l = n.bit_length()
        ans = 2

        for l in range(2, bit_l):
            ans += 1 << ((l - 1) // 2)
            
        MN = 1 << ((bit_l + 1) // 2 - 1)

        pre_pal = bin(n)[2:][:(bit_l + 1) // 2]
        MX = int(pre_pal, 2)
        ans += (MX - MN) # 不包含MX
        
        if bit_l % 2 == 0:
            pal = pre_pal + pre_pal[::-1]
        else:
            pal = pre_pal + pre_pal[-2::-1]


        return ans + 1 if int(pal, 2) <= n else ans # 3ms