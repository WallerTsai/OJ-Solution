class Solution:
    def minSwaps(self, s: str) -> int:
        ans = 0
        s = list(s)
        count = r = 0
        for l, c in enumerate(s):
            if c == "[":
                count += 1
            else:
                if count == 0:
                    while s[r] == "]":
                        r -= 1
                    s[l], s[r] = s[r], s[l]
                    ans += 1
                    count += 1
                else:
                    count -= 1
        return ans  # 267ms


# 2026年2月20日

class Solution:
    def minSwaps(self, s: str) -> int:
        s = list(s)
        ans = count = 0
        right = len(s) - 1
        for left, ch in enumerate(s):
            if ch == '[':
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    while s[right] == ']':
                        right -= 1
                    s[left], s[right] = s[right], s[left]
                    ans += 1
                    count += 1
        return ans  # 243ms

class Solution:
    # 灵神
    def minSwaps(self, s: str) -> int:
        ans = count = 0
        for ch in s:
            if ch == '[':
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    ans += 1
                    count += 1
        return ans  # 139ms


