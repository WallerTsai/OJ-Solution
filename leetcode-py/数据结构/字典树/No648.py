from typing import List


class Solution:
    # 前缀函数
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()
        s = sentence.split(" ")
        for i, c in enumerate(s):
            for j in dictionary:
                if c.startswith(j):
                    s[i] = j
                    break
        return " ".join(s)


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        tree = {}
        for word in dictionary:
            temp = tree
            for c in word:
                if c not in temp:
                    temp[c] = {}
                temp = temp[c]
            temp["end"] = True

        def fun(word: int) -> str:
            temp = tree
            for i, c in enumerate(word):
                if "end" in temp:
                    return word[:i]
                elif c not in temp:
                    break
                temp = temp[c]
            return word
        
        return " ".join(map(fun,sentence.split(" ")))