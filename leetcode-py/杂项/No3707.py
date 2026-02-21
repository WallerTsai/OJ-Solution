class Solution:
    def scoreBalance(self, s: str) -> bool:
        total = sum(ord(ch) - ord('a') + 1 for ch in s)
        pre = 0
        for i, ch in enumerate(s):
            pre += ord(ch) - ord('a') + 1
            if pre == total - pre:
                return True
        return False