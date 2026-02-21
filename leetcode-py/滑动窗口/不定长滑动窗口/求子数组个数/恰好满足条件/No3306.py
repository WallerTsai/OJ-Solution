from collections import defaultdict


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def fun(s: str, i: int):
            cnt = defaultdict(int)
            ans = count = left = 0
            for w in word:
                if w in "aeiou":
                    cnt[w] += 1
                else:
                    count += 1
                
                while len(cnt) == 5 and count >= i:
                    out = word[left]
                    if out in "aeiou":
                        cnt[out] -= 1
                        if cnt[out] == 0:
                            cnt.pop(out)
                    else:
                        count -= 1
                    left += 1
                ans += left
            return ans 
        return fun(word,k) - fun(word,k+1)
    
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def fun(i: int):
            cnt = defaultdict(int)
            ans = count = left = 0
            for w in word:
                if w in "aeiou":
                    cnt[w] += 1
                else:
                    count += 1
                
                while len(cnt) == 5 and count >= i:
                    out = word[left]
                    if out in "aeiou":
                        cnt[out] -= 1
                        if cnt[out] == 0:
                            cnt.pop(out)
                    else:
                        count -= 1
                    left += 1
                ans += left
            return ans 
        return fun(k) - fun(k+1)