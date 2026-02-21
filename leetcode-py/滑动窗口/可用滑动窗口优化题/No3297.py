from collections import Counter, defaultdict
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            return 0

        cnt = Counter(word2)
        need = len(cnt)
        res = left = 0
        
        need_cnt  = Counter()

        for c in word1:
            need_cnt[c] += 1

            if need_cnt[c] == cnt[c]:
                need -= 1

            while need == 0:
                if need_cnt[word1[left]] == cnt[word1[left]]:
                    need += 1
                need_cnt[word1[left]] -= 1
                left += 1
            res += left
        return res

# class Solution:
#     def validSubstringCount(self, word1: str, word2: str) -> int:
#         if len(word1) < len(word2):
#             return 0
        
#         cnt = Counter(word2)
#         need = len(cnt)
#         res = left = 0

#         for c in word1:
#             if c not in cnt:
#                 continue
#             cnt[c] -= 1
#             if cnt[c] == 0:
#                 need -= 1
#             while need == 0:
#                 if word1[left] in cnt:
#                     if cnt[word1[left]] == 0:
#                         need += 1
#                     cnt[word1[left]] += 1
#                 left += 1
#             res += left
#         return res

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
        return res  # 271ms

class Solution:
    # leetcode 最快
    def validSubstringCount(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0

        # t 的字母出现次数与 s 的字母出现次数之差
        diff = defaultdict(int)  # 也可以用 Counter(t)，但是会慢很多
        for c in t:
            diff[c] += 1

        # 窗口内有 less 个字母的出现次数比 t 的少
        less = len(diff)

        ans = left = 0
        for c in s:
            diff[c] -= 1
            if diff[c] == 0:
                # c 移入窗口后，窗口内 c 的出现次数和 t 的一样
                less -= 1
            while less == 0:  # 窗口符合要求
                if diff[s[left]] == 0:
                    # s[left] 移出窗口之前，检查出现次数，
                    # 如果窗口内 s[left] 的出现次数和 t 的一样，
                    # 那么 s[left] 移出窗口后，窗口内 s[left] 的出现次数比 t 的少
                    less += 1
                diff[s[left]] += 1
                left += 1
            ans += left
        return ans