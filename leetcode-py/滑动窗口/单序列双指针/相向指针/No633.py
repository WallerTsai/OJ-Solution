from math import isqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        right = isqrt(c)
        left = 0
        while left <= right:
            num = left**2 + right**2
            if num > c:
                right -= 1
            elif num < c:
                left += 1
            else:
                return True
        return False