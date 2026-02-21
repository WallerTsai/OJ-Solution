from collections import Counter, defaultdict



class Solution:
    # 分治,递归
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        for i,c in enumerate(s):
            if c.upper() not in s or c.lower() not in s:
                return max(self.longestNiceSubstring(s[:i]),self.longestNiceSubstring(s[i+1:]),key=len)
        return s

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        res = ""
        left = right = 0


# 如果是美好的，那么它字母数量一定是全小写字母数量的二倍
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) == 1:
            return ''
        result = ''
        l = 0
        while l < len(s) - 1:
            r = l + 1
            while r < len(s):
                if len(set(s[l:r+1])) == len(set(s[l:r+1].lower())) * 2:
                    if len(s[l:r+1]) > len(result):
                        result = s[l:r+1]
                r += 1
            l += 1
        return result
    
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) == 1:
            return ''
        result = ''
        l = 0
        max_len = 1
        while l < len(s) - 1:
            r = l + max_len
            if r >= len(s):
                break
            while r < len(s):
                if len(set(s[l:r+1])) == len(set(s[l:r+1].lower())) * 2:
                    if len(s[l:r+1]) > len(result):
                        result = s[l:r+1]
                        max_len = r - l + 1
                r += 1
            l += 1
        return result
    

