class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        if n < 3:
            return s
        
        p1 = s[0]
        p2 = s[1]
        ans = [p1, p2]
        for ch in s[2:]:
            if not (p1 == p2 == ch):
                ans.append(ch)
            p1, p2 = p2, ch
        
        return "".join(ans) # 159ms