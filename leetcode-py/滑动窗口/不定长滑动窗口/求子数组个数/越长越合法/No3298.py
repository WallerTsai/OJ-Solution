from collections import Counter


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            return 0
        
        cnt = Counter(word2)
        need = len(cnt)

        res = left = 0
        cur_cnt = Counter()

        for c in word1:
            cur_cnt[c] += 1

            if cur_cnt[c] == cnt[c]:
                need -= 1

            while need == 0:
                if cur_cnt[word1[left]] == cnt[word1[left]]:
                    need += 1
                cur_cnt[word1[left]] -= 1
                left += 1
            res += left

        return res # 3472ms
    
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            return 0
        
        cnt = Counter(word2)
        need = len(cnt)
        res = left = 0

        for c in word1:
            if c in cnt:
                cnt[c] -= 1
                if cnt[c] == 0:
                    need -= 1
            while need == 0:
                if word1[left] in cnt:
                    if cnt[word1[left]] == 0:
                        need += 1
                    cnt[word1[left]] += 1
                left += 1
            res += left
        return res  # 2815
