class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        count = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == '0':
                i += 1
                continue
            i += 1
            while i < n and s[i] == s[i - 1] == '1':
                i += 1
            count += 1
        return count <= 1
    

class Solution:
    # 灵神
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s