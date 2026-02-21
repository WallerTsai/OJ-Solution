from math import inf


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            return str(int(n) - 1)

        def generate_palindromes(base: int):

            while True:
                # 生成奇数长度回文数，例如 base = 10，生成的范围是 101 ~ 999
                for i in range(base, base * 10):
                    s = str(i)
                    x = s + s[::-1][1:]
                    yield x
                # 生成偶数长度回文数，例如 base = 10，生成的范围是 1001 ~ 9999
                for i in range(base, base * 10):
                    s = str(i)
                    x = s + s[::-1]
                    yield x
                

        pre = "0"
        for i in range(-1,1):
            base = 10 ** max(1, (length + 1) // 2 + i)
            for x in generate_palindromes(base):
                if x >= n:
                    return pre
                pre = x # 错误


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            return str(int(n) - 1)
        
        if n == n[::-1]:
            mid = n[length // 2]
            i = int(mid)
            if mid == "0":
                half  = int(n[: (length + 1) // 2])
                half_s = str(half - 1)
                if length % 2:
                    s1 = half_s[:-1] + half_s[-1] + half_s[:-1][::-1]
                else:
                    s1 = half_s + half_s[::-1]

                s2 = n[:]
                s2[length // 2] = str(i + 1)
                if length % 2 == 0:
                    s2[length // 2 + 1] = str(i + 1)
                    
            elif mid == "9":
                s1 = n[:]
                s1[length // 2] = str(i - 1)
                if length % 2 == 0:
                    s1[length // 2 + 1] = str(i - 1)

                half  = int(n[: (length + 1) // 2])
                half_s = str(half + 1)
                if length % 2:
                    s2 = half_s[:-1] + half_s[-1] + half_s[:-1][::-1]
                else:
                    s2 = half_s + half_s[::-1]
            else:
                s1 = n[:]
                s1[length // 2] = str(i - 1)
                if length % 2 == 0:
                    s1[length // 2 + 1] = str(i - 1)
                    
                s2 = n[:]
                s2[length // 2] = str(i + 1)
                if length % 2 == 0:
                    s2[length // 2 + 1] = str(i + 1)

            return min(s1, s2, key=lambda x: (abs(x - n), x))

        if length % 2:
            return n[ : length//2 + 1] + n[: length//2][::-1]
        else:
            return n[: length//2] + n[: length//2][::-1]    # 错误
        

class Solution:
    # jam
    def nearestPalindromic(self, n: str) -> str:
        m = int(n)
        length = len(n)

        # 0 - 9 和 10 ^ n :
        if m < 10 or m == 10 ** (length - 1):
            return str(m - 1)
        
        # 10 ^ n - 1 ：
        if m == 10 ** length - 1:
            return str(m + 2)
        
        # 10 ^ (n - 1) + 1 ：
        if m == 10 ** (length - 1) + 1:
            return str(m - 2)
        
        res = "0"
        half = int(n[:(length + 1) // 2])
        diff = inf
        for dx in (-1, 0, 1):
            new_half_s = str(half + dx)
            s = new_half_s[:length // 2] + new_half_s[::-1]

            if s == n:
                continue

            d = abs(m - int(s))
            if d < diff:
                res = s
                diff = d

        return res