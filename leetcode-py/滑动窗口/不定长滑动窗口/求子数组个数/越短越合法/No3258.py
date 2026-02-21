class Solution:
    # 这边思路捋一捋就出来了
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        cnt = [0] * 2
        res = left = 0
        for right,c in enumerate(s):
            cnt[int(c)] += 1
            while cnt[0] > k and cnt[1] > k:
                cnt[int(s[left])] -= 1
                left += 1
            res += right - left + 1
        return res  # 2ms



