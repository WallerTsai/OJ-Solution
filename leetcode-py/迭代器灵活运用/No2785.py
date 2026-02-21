from collections import Counter


class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s)
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        vowel_li = []
        index_li = []
        for i, ch in enumerate(s):
            if ch in vowel:
                vowel_li.append(ch)
                index_li.append(i)
        
        vowel_li.sort()
        for i, ch in zip(index_li, vowel_li):
            s[i] = ch

        return ''.join(s)   # 84ms
    
class Solution:
    # 灵神
    # 迭代器
    def sortVowels(self, s: str) -> str:
        VOWELS = "AEIOUaeiou"
        cnt = Counter(ch for ch in s if ch in VOWELS)

        it = iter(VOWELS)
        cur = next(it)

        t = list(s)  # str 无法修改，转成 list
        for i, ch in enumerate(t):
            if ch in VOWELS:
                if cnt[cur] == 0:
                    # 找下一个出现次数大于 0 的元音字母
                    cur = next(c for c in it if cnt[c])
                t[i] = cur
                cnt[cur] -= 1
        return ''.join(t)