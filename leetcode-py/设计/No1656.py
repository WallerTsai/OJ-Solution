from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.values = [None for _ in range(n+1)]

    def insert(self, idKey: int, value: str) -> List[str]:
        self.values[idKey] = value
        res = []
        if idKey == self.ptr:
            try:
                while self.values[self.ptr]:
                    res.append(self.values[self.ptr])
                    self.ptr += 1
            except Exception:
                pass
        return res # 33ms

class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.ptr = 1
        self.values = [None for _ in range(n+1)]

    def insert(self, idKey: int, value: str) -> List[str]:
        self.values[idKey] = value
        res = []
        if idKey == self.ptr:
            while self.ptr <= self.n and self.values[self.ptr] :
                res.append(self.values[self.ptr])
                self.ptr += 1
        return res # 14ms
    
class OrderedStream:

    def __init__(self, n: int):
        self._n = n
        self._ptr = 1
        self._values = [None for _ in range(n+1)]

    def insert(self, idKey: int, value: str) -> List[str]:
        self._values[idKey] = value
        if idKey == self._ptr:
            while self._ptr <= self._n and self._values[self._ptr] :
                self._ptr += 1
            return self._values[idKey:self._ptr]
        return [] # 4ms


class TextEditor:
    # 对顶栈
    # 灵神
    def __init__(self):
        self.left = []  # 光标左侧字符
        self.right = []  # 光标右侧字符

    def addText(self, text: str) -> None:
        self.left.extend(text)  # 入栈

    def deleteText(self, k: int) -> int:
        pre = len(self.left)  # 删除之前的栈大小
        del self.left[-k:]  # 出栈
        return pre - len(self.left)  # 减去删除之后的栈大小

    def text(self) -> str:
        return ''.join(self.left[-10:])  # 光标左边至多 10 个字符

    def cursorLeft(self, k: int) -> str:
        while k and self.left:
            self.right.append(self.left.pop())  # 左手倒右手
            k -= 1
        return self.text()

    def cursorRight(self, k: int) -> str:
        while k and self.right:
            self.left.append(self.right.pop())  # 右手倒左手
            k -= 1
        return self.text()

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)