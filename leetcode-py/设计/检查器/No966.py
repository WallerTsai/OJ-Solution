from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word: str) -> str:
            # 将字符串中元音字母转化成'*'
            res = []
            for ch in word:
                if ch in "aeiou":
                    res.append('*')
                else:
                    res.append(ch)
            return "".join(res)

        # 三个哈希表
        origin = set()
        lower_to_origin = dict()
        vovel_to_origin = dict()

        for word in wordlist:
            origin.add(word)
            lower = word.lower()
            lower_to_origin[lower] = word           # 例如 kite -> KiTe
            vovel_to_origin[devowel(lower)] = word  # 例如 k?t? -> KiTe

        for i, q in enumerate(queries):
            if q in origin:
                continue
            lower = q.lower()
            if lower in lower_to_origin:
                queries[i] = lower_to_origin[lower]
            elif devowel(lower) in vovel_to_origin:
                queries[i] = vovel_to_origin[devowel(lower)]
            else:
                queries[i] = ""

        return queries  # 还有一个细节没有做好 顺序问题
    
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word: str) -> str:
            # 将字符串中元音字母转化成'*'
            res = []
            for ch in word:
                if ch in "aeiou":
                    res.append('*')
                else:
                    res.append(ch)
            return "".join(res)

        # 三个哈希表
        origin = set()
        lower_to_origin = dict()
        vovel_to_origin = dict()

        for word in reversed(wordlist):
            origin.add(word)
            lower = word.lower()
            lower_to_origin[lower] = word           # 例如 kite -> KiTe
            vovel_to_origin[devowel(lower)] = word  # 例如 k?t? -> KiTe

        for i, q in enumerate(queries):
            if q in origin:
                continue
            lower = q.lower()
            if lower in lower_to_origin:
                queries[i] = lower_to_origin[lower]
            elif devowel(lower) in vovel_to_origin:
                queries[i] = vovel_to_origin[devowel(lower)]
            else:
                queries[i] = ""

        return queries 
    

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word: str) -> str:
            # 将字符串中元音字母转化成'*'
            res = []
            for ch in word:
                if ch in "aeiou":
                    res.append('*')
                else:
                    res.append(ch)
            return "".join(res)

        # 三个哈希表
        origin = set()
        lower_to_origin = dict()
        vowel_to_origin = dict()

        for word in wordlist:
            origin.add(word)
            lower = word.lower()
            lower_to_origin.setdefault(lower, word)          # 例如 kite -> KiTe
            vowel_to_origin.setdefault(devowel(lower), word)  # 例如 k?t? -> KiTe

        for i, q in enumerate(queries):
            if q in origin:
                continue
            lower = q.lower()
            if lower in lower_to_origin:
                queries[i] = lower_to_origin[lower]
            else:
                queries[i] = vowel_to_origin.get(devowel(lower), "")

        return queries