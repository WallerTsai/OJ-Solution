class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        text = text.split()
        for word in text:
            for ch in word:
                if ch in brokenLetters:
                    ans += 1
                    break
        return len(text) - ans
    

class Solution:
    # 灵神
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_mask = 0
        for c in brokenLetters:
            broken_mask |= 1 << (ord(c) - ord('a'))  # 把 c 加到集合中

        ans = 0
        ok = True
        for c in text:
            if c == ' ':  # 上一个单词遍历完毕
                ans += ok
                ok = True
            elif broken_mask >> (ord(c) - ord('a')) & 1:  # c 在 brokenLetters 中
                ok = False
        ans += ok  # 最后一个单词
        return ans