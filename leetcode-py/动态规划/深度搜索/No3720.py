from collections import Counter, defaultdict
from string import ascii_lowercase


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = defaultdict(int)
        for ch in s:
            cnt[ord(ch)] += 1
        ans = []
        for ch in target:
            flag = False
            for _ord in range(ord(ch), ord('z') + 1):
                if _ord in cnt:
                    cnt[_ord] -= 1
                    if cnt[_ord] == 0:
                        del cnt[_ord]
                    ans.append(chr(_ord))
                    flag = True
                    break
            if not flag:
                return ""
        return ''.join(ans) # 错误
                

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = defaultdict(int)
        for ch in s:
            cnt[ord(ch)] += 1
        ans = []
        for ch in target:
            if ord(ch) in cnt:
                cnt[ord(ch)] -= 1
                if cnt[ord(ch)] == 0:
                    del cnt[ord(ch)]
                ans.append(ch)
            else:
                for _ord in range(ord(ch) + 1, ord('z') + 1):
                    if _ord in cnt:
                        cnt[_ord] -= 1
                        if cnt[_ord] == 0:
                            del cnt[_ord]
                        ans.append(chr(_ord))
                        for k in sorted(cnt.keys()):
                            for _ in range(cnt[k]):
                                ans.append(chr(k))
                        return ''.join(ans)
        for i in range(len(ans)-2, -1, -1):
            if ans[i] != ans[i + 1]:
                ans = ans[:i] + list(sorted(ans[i:], reverse= True))
                if ''.join(ans) > target:
                    return ''.join(ans)

        return ""   # 错误      
    
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        
        # 特判
        max_s = ''.join(sorted(s, reverse=True))
        if max_s <= target:
            return ""
        
        res = []
        found = False
        
        def dfs(pos, flag):
            nonlocal found
            if found:
                return True
            if pos == n:
                if flag:
                    found = True
                    return True
                return False    # 完全相同

            if flag:    # 这一位已经大于对应target位置上的数字，后面按最小字典排序
                for ch in sorted(cnt.keys()):
                    if cnt[ch] > 0:
                        res.append(ch)
                        cnt[ch] -= 1
                        if dfs(pos + 1, True):
                            return True
                        cnt[ch] += 1
                        res.pop()
                return False
            else:
                for ch in sorted(cnt.keys()):
                    if ch < target[pos] or cnt[ch] == 0:
                        continue
                    res.append(ch)
                    cnt[ch] -= 1
                    if ch > target[pos]:    # 这位大于对应target位置上的数字，标志位置1
                        if dfs(pos + 1, True):
                            return True
                    else:   # 相同
                        if dfs(pos + 1, False):
                            return True
                    cnt[ch] += 1
                    res.pop()
                return False
            
        dfs(0, False)
        return ''.join(res) if found else ""
    

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        
        # 特判
        max_s = ''.join(sorted(s, reverse=True))
        if max_s <= target:
            return ""
        
        res = []
        found = False
        
        def dfs(pos, flag):
            nonlocal found
            if found:
                return True
            if pos == n:
                if flag:
                    found = True
                    return True
                return False    # 完全相同

            if flag:    # 这一位已经大于对应target位置上的数字，后面按最小字典排序
                for ch in sorted(cnt.keys()):
                    if cnt[ch] > 0:
                        res.append(ch)
                        cnt[ch] -= 1
                        if dfs(pos + 1, True):
                            return True
                        cnt[ch] += 1
                        res.pop()
                return False
            else:
                for ch in sorted(cnt.keys()):
                    if ch < target[pos] or cnt[ch] == 0:
                        continue
                    res.append(ch)
                    cnt[ch] -= 1
                    if ch > target[pos]:    # 这位大于对应target位置上的数字，标志位置1
                        if dfs(pos + 1, True):
                            return True
                    else:   # 相同
                        if dfs(pos + 1, False):
                            return True
                    cnt[ch] += 1
                    res.pop()
                return False
            
        dfs(0, False)
        return ''.join(res) if found else ""
    
class Solution:
    # 灵神
    # 倒序贪心
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        left = Counter(s)
        for c in target:
            left[c] -= 1  # 消耗 s 中的一个字母 c

        neg, mx = 0, ''
        for c, cnt in left.items():
            if cnt < 0:
                neg += 1  # 统计 left 中的负数个数
            elif cnt > 0:
                mx = max(mx, c)

        ans = list(target)
        for i in range(len(s) - 1, -1, -1):
            c = target[i]
            left[c] += 1  # 撤销消耗

            if left[c] == 0:
                neg -= 1
            elif left[c] == 1:
                mx = max(mx, c)

            # left 有负数 or 没有大于 target[i] 的字母
            if neg > 0 or c >= mx:
                continue

            j = ord(c) - ord('a') + 1
            while left[ascii_lowercase[j]] == 0:
                j += 1

            # target[i] 增大到 ch
            ch = ascii_lowercase[j]
            left[ch] -= 1
            ans[i] = ch
            del ans[i + 1:]

            for ch in ascii_lowercase:
                ans.extend(ch * left[ch])
            return ''.join(ans)
        return ""
    
class Solution:
    # 妙蛙
    # 试填
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        # 检查是否存在可能的排列
        sorted_desc = ''.join(sorted(s, reverse=True))
        if sorted_desc <= target:
            return ""
        
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        
        ans = []
        
        # 检查当前位能不能填 c
        def can_fill(c):
            tmp = ans + [chr(c + ord('a'))]
            # 剩下的字母从大到小填到后面的位里
            remaining = []
            for d in range(25, -1, -1):
                remaining.extend([chr(d + ord('a'))] * cnt[d])
            tmp.extend(remaining)
            return ''.join(tmp) > target
        
        # 从左到右枚举每一位
        for i in range(n):
            # 从小到大枚举这一位能不能填 c
            for c_idx in range(26):
                if cnt[c_idx] > 0:
                    cnt[c_idx] -= 1
                    if can_fill(c_idx):
                        ans.append(chr(c_idx + ord('a')))
                        break
                    cnt[c_idx] += 1
        
        return ''.join(ans)
    


# 2026年2月10日
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        if ''.join(sorted(s, reverse=True)) <= target:
            return ""
        
        n = len(s)
        cnt = Counter(s)

        res = []
        found = False
        sorted_keys = sorted(cnt.keys())
        def dfs(idx: int, flag: bool):
            nonlocal found
            if found:   # 从这里可以看出，应该写贪心
                return True 
            if idx == n:
                if not flag:    # 全部相等
                    return False
                found = True
                return True
            # 前面已经存在一个比target对应位置大的字符
            if flag:
                for ch in sorted_keys:
                    if cnt[ch] == 0:
                        continue
                    res.append(ch)
                    cnt[ch] -= 1
                    if dfs(idx + 1, True):
                        return True
                    # 恢复现场
                    cnt[ch] += 1
                    res.pop()
                return False
            else:
                for ch in sorted_keys:
                    if ch < target[idx] or cnt[ch] == 0:
                        continue
                    res.append(ch)
                    cnt[ch] -= 1
                    if dfs(idx + 1, ch > target[idx]):
                        return True
                    res.pop()
                    cnt[ch] += 1
                return False
            
        dfs(0, False)
        return ''.join(res) if found else ""
                


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        if ''.join(sorted(s, reverse=True)) <= target:
            return ""
        
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        res =  []

        def can_fill(ch: str):
            temp = res + [chr(ch + ord('a'))]
            remaining = []
            for d in range(25, -1, -1):
                remaining.extend([chr(d + ord('a'))] * cnt[d])
            temp.extend(remaining)
            return ''.join(temp) > target
        
        for _ in range(n):
            for ch_idx in range(26):
                if cnt[ch_idx] == 0:
                    continue
                cnt[ch_idx] -= 1
                if can_fill(ch_idx):
                    res.append(chr(ch_idx + ord('a')))
                    break
                cnt[ch_idx] += 1
        
        return ''.join(res)




