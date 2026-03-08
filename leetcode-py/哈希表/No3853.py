from collections import defaultdict


class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        ans = []
        cnt = defaultdict(int)
        t = 0
        for i, ch in enumerate(s):
            if ch not in cnt or i - cnt[ch] - t > k:
                ans.append(ch)
            else:
                t += 1
                continue
            cnt[ch] = i - t
        return ''.join(ans)