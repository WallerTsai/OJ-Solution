
class Solution:
    def lexSmallest(self, s: str) -> str:
        ans = s
        for i in range(1, len(s)):
            temp1 = s[i::-1] + s[i + 1:]
            temp2 = s[:i] + s[-1:i - 1:-1]
            ans = min(ans, temp1, temp2)
        return ans


class Solution:
    def lexSmallest(self, s: str) -> str:
        ans = s  # k = 1 时，操作不改变 s
        for k in range(2, len(s) + 1):
            ans = min(ans, s[:k][::-1] + s[k:], s[:-k] + s[-k:][::-1])
        return ans