from itertools import count


class Solution:
    # https://leetcode.cn/problems/minimum-operations-to-make-the-integer-zero/solutions/2319632/mei-ju-da-an-pythonjavacgo-by-endlessche-t4co/
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in count(1):
            x = num1 - num2 * i
            if i > x:
                return -1
            if i >= x.bit_count():
                return i

