class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        _set = set()
        for i in range(k, len(s) + 1):
            _set.add(s[i - k: i])
        return len(_set) == pow(2, k)

class Solution:
    # 灵神
    def hasAllCodes(self, s: str, k: int) -> bool:
        MASK = (1 << k) - 1
        st = set()  # 更快的写法见另一份代码【Python3 列表】
        x = 0
        for i, ch in enumerate(s):
            # 把 ch 加到 x 的末尾：x 整体左移一位，然后或上 ch
            # &MASK 目的是去掉超出 k 的比特位
            x = (x << 1 & MASK) | int(ch)
            if i >= k - 1:
                st.add(x)
        return len(st) == 1 << k

