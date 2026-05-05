def kmp_search(text, pattern, separator="#"):
    if not pattern:
        return []
        
    s = pattern + separator + text
    m = len(pattern)
    n = len(s)
    
    nxt = [0] * n
    j = 0 
    res = []
    
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = nxt[j - 1]
            
        if s[i] == s[j]:
            j += 1
            
        nxt[i] = j
        
        if j == m:
            res.append(i - 2 * m)
            
    return res


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        s = s + s
        res = kmp_search(s, goal)
        if res:
            return True
        return False