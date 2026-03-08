class Solution:
    def minOperations(self, s: str) -> int:
        pre = s[0]
        ans = 0
        for i in range(1, len(s)):
            ch = s[i]
            if ch == pre:
                ans += 1
                pre = '1' if ch == '0' else '0'
                continue
            pre = ch
        return ans # 错误
    


class Solution:
    # 灵神
    def minOperations(self, s: str) -> int:
        diff = 0
        for i, ch in enumerate(s):
            # 如果 i 是偶数，把 ch 变成 0，否则变成 1
            if int(ch) != i % 2:
                diff += 1
        return min(diff, len(s) - diff)