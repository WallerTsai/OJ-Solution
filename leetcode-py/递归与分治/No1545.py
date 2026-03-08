class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        if k == 1 << (n - 1):
            return '1'
        # 左半部分
        if k < 1 << (n - 1):
            return self.findKthBit(n - 1, k)
        # 右半部分
        res = self.findKthBit(n - 1, (1 << n) - k)
        return '0' if res == '1' else '1'


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        rev = 0
        while True:
            if n == 1:
                return '1' if rev else '0'
            if k == 1 << (n - 1):
                return '0' if rev else '1'
            if k > 1 << (n - 1):
                k = (1 << n) - k
                rev ^= 1
            n -= 1
            