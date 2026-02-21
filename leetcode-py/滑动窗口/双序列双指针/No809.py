from itertools import groupby
from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def check_byone(s:str,word:str) -> bool:
            if len(s) < len(word):
                return False
            p1 = p2 = 0
            while p1 < len(s) and p2 < len(word):
                if s[p1] != word[p2]:
                    return False
                
                cnt_1 = cnt_2 = 1

                while p1 < len(s)-1 and s[p1] == s[p1+1]:
                    p1 += 1
                    cnt_1 += 1
                while p2 < len(word)-1 and word[p2] == word[p2+1]:
                    p2 += 1
                    cnt_2 += 1

                if cnt_1 < cnt_2 or (cnt_1 < 3 and cnt_1 != cnt_2):
                    return False

                p1 += 1
                p2 += 1
            return p1 == len(s) and p2 == len(word)
        
        res = 0
        for word in words:
            res += check_byone(s,word)
        return res  # 11ms
    
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        model = [(key,len(list(value))) for key,value in groupby(s)]
        res = 0
        for word in words:
            if len(s) < len(word):
                continue
            temp = [(key,len(list(value))) for key,value in groupby(word)]
            if len(model) != len(temp):
                continue
            flag = True
            for (c1,n1),(c2,n2) in zip(model,temp):
                if c1 != c2:
                    flag = False
                    break
                if n1 < n2 or (n1 < 3 and n1 != n2):
                    flag = False
                    break
            if flag:
                res += 1
        return res  # 11ms
    
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        model = [(key,len(list(value))) for key,value in groupby(s)]
        res = 0
        for word in words:
            if len(s) < len(word):
                continue
            
            p1 = p2 = 0
            while p1 < len(model) and p2 < len(word):
                c,cnt1 = model[p1]
                if c != word[p2]:
                    break
                cnt2 = 1
                while p2 < len(word)-1 and word[p2] == word[p2+1]:
                    p2 += 1
                    cnt2 += 1

                if cnt1 < cnt2 or (cnt1 < 3 and cnt1 != cnt2):
                    break

                p1 += 1
                p2 += 1

            if p1 == len(model) and p2 == len(word):
                res += 1

        return res  # 3ms

fun = Solution()
outcome = fun.expressiveWords("heeellooo",["hello", "hi", "helo"])
print(outcome)
