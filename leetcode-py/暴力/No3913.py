from collections import defaultdict


class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s)
        cnt = defaultdict(int)
        for ch in s:
            if ch in "aeiou":
                cnt[ch] += 1
        
        li = []
        for ch, count in sorted(cnt.items(), key=lambda x : x[1], reverse=True):
            li.extend([ch] * count)

        i = 0
        for j in range(len(s)):
            if s[j] in "aeiou":
                s[j] = li[i]
                i += 1
        return ''.join(s)