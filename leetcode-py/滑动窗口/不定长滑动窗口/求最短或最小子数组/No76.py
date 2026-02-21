from collections import defaultdict,Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        need = Counter(t)
        
        length = len(t)

        res = ''
        left = 0
        for right,c in enumerate(s):

            if c in need:
                if need[c] > 0:
                    length -= 1
                need[c] -= 1

            if length == 0:
                # 滑(注意条件)
                while True:
                    if s[left] in need:
                        if need[s[left]] < 0:
                            need[s[left]] += 1
                        else:
                            break
                    left += 1
                # 更新
                if right - left + 1 < len(res) or (not res):
                    res = s[left:right+1]
                # 处理尾巴
                length += 1
                need[s[left]] += 1
                left += 1
        return res
