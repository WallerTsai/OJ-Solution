from itertools import count


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        res = ""
        length = len(s) + 1
        left = cnt = 0
        for right,c in enumerate(s):
            if c == '1':
                cnt += 1
            while cnt > k:
                if s[left] == '1':
                    cnt -= 1
                left += 1
            if cnt == k:
                while s[left] != '1':
                    left += 1
                if right - left + 1 < length:
                    res = s[left:right+1]
                    length = right - left + 1
                elif right - left + 1 == length:
                    if int(s[left:right+1]) < int(res):
                        res = s[left:right+1]
        return res  # 0ms

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        res = ""
        length = len(s) + 1
        left = cnt = 0
        for right,c in enumerate(s):
            if c == '1':
                cnt += 1
            while cnt > k:
                if s[left] == '1':
                    cnt -= 1
                left += 1
            if cnt == k:
                while s[left] != '1':
                    left += 1
                if right - left + 1 < length:
                    res = s[left:right+1]
                    length = right - left + 1
                elif right - left + 1 == length:
                    if int(s[left:right+1]) < int(res):
                        res = s[left:right+1]
        return res

class Solution:
    # 灵神
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # 1 的个数不足 k
        if s.count('1') < k:
            return ''
        # 否则一定有解
        for size in count(k):  # 从 k 开始枚举
            ans = ''
            for i in range(size, len(s) + 1):
                t = s[i - size: i]
                if (ans == '' or t < ans) and t.count('1') == k:
                    ans = t
            if ans: return ans

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        res = ""
        if s.count('1') < k:
            return res
        length = len(s) + 1
        left = cnt = 0
        for right,c in enumerate(s):
            if c == '1':
                cnt += 1
            while cnt > k or s[left] != '1':
                if s[left] == '1':
                    cnt -= 1
                left += 1
            if cnt == k:
                if right - left + 1 < length:
                    res = s[left:right+1]
                    length = right - left + 1
                elif right - left + 1 == length:
                    if int(s[left:right+1]) < int(res):
                        res = s[left:right+1]
        return res