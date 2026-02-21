class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))
        for i, ch in enumerate(s):
            if ch == "6":
                s[i] = "9"
                break
        return int("".join(s))


class Solution:
    def maximum69Number(self, num: int) -> int:
        s = str(num).replace('6', '9', 1)  # 替换第一个 6
        return int(s)


class Solution:
    def maximum69Number(self, num: int) -> int:
        max_base = 0
        base = 1
        x = num
        while x:
            x, d = divmod(x, 10)
            if d == 6:
                max_base = base
            base *= 10
        return num + max_base * 3