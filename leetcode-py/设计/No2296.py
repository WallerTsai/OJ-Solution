class TextEditor:

    def __init__(self):
        self.text = ""
        self.cursor = 0

    def addText(self, text: str) -> None:
        self.text = self.text[:self.cursor] + text + self.text[self.cursor:]
        self.cursor += len(text)
        
    def deleteText(self, k: int) -> int:
        pre = self.cursor
        self.text = self.text[0:max(self.cursor - k,0)] + self.text[self.cursor:]
        self.cursor -= k
        self.cursor = max(0,self.cursor)
        return min(pre - self.cursor,k)

    def cursorLeft(self, k: int) -> str:
        self.cursor -= k
        self.cursor = max(0,self.cursor)
        return self.text[max(self.cursor - 10,0):self.cursor]

    def cursorRight(self, k: int) -> str:
        self.cursor += k
        self.cursor = min(len(self.text),self.cursor)
        return self.text[max(self.cursor - 10,0):self.cursor]
    # 1687ms