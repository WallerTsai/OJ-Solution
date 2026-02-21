from string import ascii_lowercase
from typing import Callable, List
class Solution:
    def reverseByType(self, s: str) -> str:
        li1 = []
        li2 = []
        idx_li1 = []
        idx_li2 = []
        s = list(s)
        for i, ch in enumerate(s):
            if ch in ascii_lowercase:
                idx_li1.append(i)
                li1.append(ch)
            else:
                idx_li2.append(i)
                li2.append(ch)
        
        
        for idx, ch in zip(idx_li1, li1[::-1]):
            s[idx] = ch
        
        for idx, ch in zip(idx_li2, li2[::-1]):
            s[idx] = ch

        return ''.join(s)
    

class Solution:
    # 灵神
    def reverse(self, t: List[str], f: Callable[[str], bool]) -> None:
        i, j = 0, len(t) - 1
        while i < j:
            while i < j and f(t[i]):
                i += 1
            while i < j and f(t[j]):
                j -= 1
            t[i], t[j] = t[j], t[i]
            i += 1
            j -= 1

    def reverseByType(self, s: str) -> str:
        t = list(s)
        self.reverse(t, str.islower)
        self.reverse(t, lambda ch: not ch.islower())
        return ''.join(t)