class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10 ** 9 + 7

        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        for _ in range(t):
            next_cnt = [0] * 26
            for i in range(26):
                if i == 25:
                    next_cnt[0] = cnt[25]
                    next_cnt[1] += cnt[25]
                else:
                    next_cnt[i + 1] = cnt[i]
            cnt = next_cnt

        return sum(cnt) % MOD
    
# 原地修改
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10 ** 9 + 7

        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        for _ in range(t):
            cnt_z = cnt[-1]
            for i in range(25, 0, -1):
                cnt[i] = cnt[i - 1]
            cnt[0] = cnt_z
            cnt[1] = (cnt_z + cnt[1]) % MOD

        return sum(cnt) % MOD   # 2142ms