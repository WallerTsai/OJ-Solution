from collections import Counter, defaultdict


class Solution:
    # 由于答案是要过程中的的最大值，你不能直接统计全部操作，得出结果
    def maxDistance(self, s: str, k: int) -> int:
        cnt = Counter(s)


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        cnt = defaultdict(int)
        for ch in s:
            cnt[ch] += 1
            temp = k

            def fun(a: int, b: int) -> int:
                nonlocal temp
                d = min(a, b, temp)
                temp -= d
                return abs(a - b) + d * 2

            ans = max(ans, fun(cnt["N"], cnt["S"]) + fun(cnt["E"], cnt["W"]))
        return ans


class Solution:
    # 灵神
    def maxDistance(self, s: str, k: int) -> int:
        ans = x = y = 0
        for i, c in enumerate(s):
            if c == 'N': y += 1
            elif c == 'S': y -= 1
            elif c == 'E': x += 1
            else: x -= 1
            ans = max(ans, min(abs(x) + abs(y) + k * 2, i + 1))
        return ans
    


    