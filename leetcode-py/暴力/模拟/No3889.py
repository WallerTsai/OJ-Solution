from collections import Counter
from string import ascii_lowercase

class Solution:
    def mirrorFrequency(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        for i in "01234":
            ans += abs(cnt[i] - cnt[str(9 - int(i))])
        for i in range(13):
            ans += abs(cnt[ascii_lowercase[i]] - cnt[ascii_lowercase[26 - i]])
        return ans


# print(ascii_lowercase[:14])