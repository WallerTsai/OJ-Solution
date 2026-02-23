from collections import Counter


d = [1]
for i in range(1, 10):
    d.append(i * d[-1])
class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        s = str(n)
        t = 0
        while n:
            a, b = divmod(n, 10)
            t += d[b]
            n = a
        print(s)
        print(str(t))
        return Counter(s) == Counter(str(t))

Solution().isDigitorialPermutation(40558)
