# 110001

#         1 1 0
#         1 0 0

#         1 0 0
#         1 0 1

#         1 0 1
#         0 0 1


#         11001  10011 00111

#         1 0 1
#         1 0

#         1 0 1
#         0 1
        
#         0 1 1
#         0 1

#         12345 23451 34512

#         1 3 5
#         2 4

#         2 4 1
#         3 5

#         3 5 2
#         4 1

class Solution:
    def minFlips(self, s: str) -> int:
        pass


# 2026年3月7日


class Solution:
    # No1758
    def minOperations_changed(self, s: str) -> int:
        diff = 0
        for i, ch in enumerate(s):
            # 如果 i 是偶数，把 ch 变成 0，否则变成 1
            if int(ch) != i % 2:
                diff += 1
        return diff, len(s) - diff
    
    def minFlips(self, s: str) -> int:
        n = len(s)
        even, odd = self.minOperations_changed(s)
        ans = min(even, odd)
        s = s + s
        for right in range(n, 2 * n):
            left = right - n
            if int(s[left]) == left % 2:
                odd -= 1
            else:
                even -= 1
            if int(s[right]) != right % 2:
                even += 1
            else:
                odd += 1
            ans = min(ans, even, odd)
        return ans
            

class Solution:
    # 灵神
    def minFlips(self, s: str) -> int:
        ans = n = len(s)
        cnt = 0
        for i in range(n * 2 - 1):
            if ord(s[i % n]) % 2 != i % 2:
                cnt += 1
            left = i - n + 1
            if left < 0:
                continue
            ans = min(ans, cnt, n - cnt)
            if ord(s[left]) % 2 != left % 2:
                cnt -= 1
        return ans