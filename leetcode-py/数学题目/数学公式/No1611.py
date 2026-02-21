# 111
# 100
# 101
# 111
# 110

# 1000 -> 1100 -> 0100
# 1001 
# 1011
# 1010
# 1110


# 000     
# 001     001     ^
# 011             |
# 010     010     |
# 110             |
# 111             |   向上走
# 101             |
# 100     100     |


# f(x) 定义为 二进制中只有第x位为1的数变成0
# f(1) = 1
# f(2) = 2 * f(1) + 1
# f(3) = 2 * f(2) + 1
# 1000 -(f(3))-> 1100 -(1)-> 0100 -(f(3))-> 0

# 11 不用先变成 10 
# 111，110， 101 不用变成 100

# 101
# f(2) + [010 -> 101]
#         (1) + [110 -> 101]
#                 [10 -> 01]  f(2) -f(1)
# 0 -> 101
# [101]
# f(2) + 1 = [110]
# [10] -> [01]  ==  f(2) - f{1}


# [1110]
# f(3) + 1 = [1100]
# [10]
# f(2)


# [1010]
# f(3) + 1 = [1100]



# 1001001
# 0100000 + (?)

#             1001
#             0100 + (?)

#                     1
#                     0  (1)

#  1001001
# (0100000)
# (0010000)

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
           return 0
        
        m = n.bit_length()

        f = [0] * (m + 1)
        f[1] = 1
        for i in range(2, m + 1):
            f[i] = 2 * f[i - 1] + 1

        ans = 0
        def track_back(i: int):
           if i == 0:
              return 0
           l = 1 << (i.bit_length() - 1)
           return f[l.bit_length()] - track_back(i ^ l)
        
        ans = track_back(n)

        return ans  # 0ms 用时2h 



class Solution:
    # 灵神
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        k = n.bit_length()
        return (1 << k) - 1 - self.minimumOneBitOperations(n - (1 << (k - 1)))   # 3ms
    

class Solution:
    # 灵神
    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0
        while n > 0:
            lb = n & -n  # n 的最低 1
            ans = (lb << 1) - 1 - ans
            n ^= lb  # 去掉 n 的最低 1
        return ans   # 0ms