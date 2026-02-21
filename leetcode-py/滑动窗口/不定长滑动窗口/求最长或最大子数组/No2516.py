from collections import Counter


class Solution:
    # 逆向思维
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = Counter(s)
        if cnt['a'] < k or cnt['b'] < k or cnt['c'] < k:
            return -1
        res = left = 0
        for right,c in enumerate(s):
            cnt[c] -= 1
            while cnt[c] < k:
                cnt[s[left]] += 1
                left += 1
            res = max(res,right-left+1)
        return len(s) - res # 231ms

class Solution:
    # 逆向思维
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = Counter(s)
        if cnt['a'] < k or cnt['b'] < k or cnt['c'] < k:
            return -1
        left = 0
        for right,c in enumerate(s):
            cnt[c] -= 1
            if cnt['a'] < k or cnt['b'] < k or cnt['c'] < k:
                cnt[s[left]] += 1
                left += 1
            
        return len(s) - (right-left+1)  # 182ms
    
class Solution:
    # leetcode最快
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0: return 0
        s = [ord(c) - ord('a') for c in s]
        rem = [-k] * 3
        for i in s: rem[i] += 1
        #if any(v < 0 for v in rem): return -1
        if min(rem) < 0: return -1
        l = -1
        for i in s:
            rem[i] -= 1
            if rem[0] < 0 or rem[1] < 0 or rem[2] < 0:
                rem[s[l := l + 1]] += 1
        '''
                count = [0] * 3
        n = len(s)

        for c in s:
            count[ord(c) - ord("a")] += 1

        for i in range(3):
            if count[i] < k:
                return -1

        window = [0] * 3
        left, max_window = 0, 0

        for right in range(n):
            window[ord(s[right]) - ord("a")] += 1

            while left <= right and (
                count[0] - window[0] < k
                or count[1] - window[1] < k
                or count[2] - window[2] < k
            ):
                window[ord(s[left]) - ord("a")] -= 1
                left += 1

            max_window = max(max_window, right - left + 1)
        '''
        return l + 1