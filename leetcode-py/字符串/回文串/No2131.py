from collections import Counter, defaultdict
from typing import List


class Solution:
    # 分类讨论, 统计
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter(words)

        ans = temp = 0
        for w, c in cnt.items():
            if w[0] == w[1]:
                if c % 2:
                    ans += c - 1
                    temp = 1
                else:
                    ans += c
            elif w[0] < w[1]:
                ans += min(c, cnt[w[::-1]]) * 2

        return (ans + temp) * 2
    
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = defaultdict(int)
        ans = 0

        for word in words:
            if cnt[word[::-1]] >= 1:
                cnt[word[::-1]] -= 1
                ans += 4
            else:
                cnt[word] += 1

        for word in cnt:
            if word[0] == word[1] and cnt[word] == 1:
                ans += 2
                break
        
        return ans