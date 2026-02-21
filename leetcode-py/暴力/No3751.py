from itertools import pairwise


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0
        for num in range(max(num1, 100), num2 + 1):
            s = str(num)
            pre = s[0]
            for a, b in pairwise(s):
                if (a > pre and a > b) or (a < pre and a < b):
                    ans += 1
                pre = a
        return ans