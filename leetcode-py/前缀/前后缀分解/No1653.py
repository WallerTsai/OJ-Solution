class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        num_a = 0
        num_b = s.count('b')
        l = 0
        s += '#'
        for ch in s:
            if ch == 'a':
                num_a += 1
            else:
                l = max(l, num_a + num_b)
                num_b -= 1
        return n - l if l else 0    # 171ms
    

class Solution:
    # 灵神
    def minimumDeletions(self, s: str) -> int:
        ans = delete = s.count('a')
        for c in s:
            delete -= 1 if c == 'a' else -1
            if delete < ans:  # 手动 min 会快很多
                ans = delete
        return ans  # 183ms
    

class Solution:
    # 灵神
    # DP
    def minimumDeletions(self, s: str) -> int:
        f = cnt_b = 0
        for c in s:
            if c == 'b': cnt_b += 1  # f 值不变
            else: f = min(f + 1, cnt_b)
        return f