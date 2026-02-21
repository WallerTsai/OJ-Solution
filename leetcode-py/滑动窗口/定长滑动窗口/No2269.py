class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        res = 0
        for i in range(k,len(s)):
            n = int(s[i-k:i+1])
            if n != 0:
                if num % n == 0:
                    res += 1

        return res

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        m = 10 ** k
        ans = 0
        n = num
        while n >= m // 10:
            x = n % m
            if x > 0 and num % x == 0:
                ans += 1
            n //= 10
        return ans
