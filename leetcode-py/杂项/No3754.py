class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)
        x = 0
        ans = ""
        for ch in s:
            if ch != "0":
                ans = ans + ch
                x += int(ch)
        return int(ans) * x if ans else 0
    

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)
        x = 0
        ans = ""
        for ch in s:
            if ch != "0":
                ans = ans + ch
                x += int(ch)
        return int(ans) * x if ans else 0
    
    
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x, s, pow10 = 0, 0, 1
        while n:
            n, d = divmod(n, 10)
            if d > 0:
                x += d * pow10
                s += d
                pow10 *= 10
        return x * s