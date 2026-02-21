class Solution:
    # 暴力
    def binaryGap(self, n: int) -> int:
        s = bin(n)[2:]
        res = pre = 0
        for i,c in enumerate(s):
            if c == '1':
                res = max(res,i-pre)
                pre = i
        return res

class Solution:
    def binaryGap(self, n: int) -> int:
        last, ans, i = -1, 0, 0
        while n:
            if n & 1:
                if last != -1:
                    ans = max(ans, i - last)
                last = i
            n >>= 1
            i += 1
        return ans
