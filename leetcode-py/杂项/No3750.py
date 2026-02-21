class Solution:
    def minimumFlips(self, n: int) -> int:
        a = bin(n)
        a = a[2:]
        ans = 0
        for x, y in zip(a, a[::-1]):
            if x != y:
                ans += 1
        return ans

class Solution:
    def minimumFlips(self, n: int) -> int:
        s = bin(n)[2:]
        ans = 0
        for i in range(len(s) // 2):
            if s[i] != s[-1 - i]:
                ans += 2
        return ans

print("a" > "1")