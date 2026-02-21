class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowol = "aeiou"
        for ch in s:
            if ch in vowol:
                return True
        return False
    
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(c in "aeiou" for c in s)