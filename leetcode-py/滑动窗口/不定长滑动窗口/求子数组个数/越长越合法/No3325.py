from collections import Counter


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        record = [0] * 26
        res = left = 0
        for right,c in enumerate(s):
            record[ord(c) - 97] += 1
            while max(record) >= k:
                record[ord(s[left]) - 97] -= 1
                left += 1
            res += left
        return res  # 27ms

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        letf = ans = 0
        cnt = Counter()
        for c in s:
            cnt[c] += 1
            while cnt[c] >= k:
                out = s[letf]
                cnt[out] -= 1
                letf += 1
            ans += letf
        return ans  # 13ms

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        record = [0] * 26
        res = left = 0
        for right,c in enumerate(s):
            record[ord(c) - 97] += 1
            while record[ord(c) - 97] >= k:
                record[ord(s[left]) - 97] -= 1
                left += 1
            res += left
        return res  # 7ms