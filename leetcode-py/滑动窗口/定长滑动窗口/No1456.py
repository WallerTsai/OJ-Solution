class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        count = 0
        yuan = "aeiou"
        for i,char in enumerate(s):
            if char in yuan:
                count += 1
            if i < k -1:
                continue

            res = max(res,count)

            if s[i-k+1] in yuan:
                count -= 1
        return res  # 109ms
    
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        count = 0
        yuan = "aeiou"
        for i,char in enumerate(s):
            if char in yuan:
                count += 1
                res = max(res,count)
            if i < k -1:
                continue


            if s[i-k+1] in yuan:
                count -= 1
        return res # 71ms
    
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        yuan = "aeiou"
        count = sum(1 for char in s[:k] if char in yuan)
        res = count
        for i in range(k,len(s)):
            if s[i-k] in yuan:
                count -= 1
            if s[i] in yuan:
                count += 1
                res = max(res,count)

        return res  # 68ms