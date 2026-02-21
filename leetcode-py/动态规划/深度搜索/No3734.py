from collections import Counter
from string import ascii_lowercase


class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        odd = 0
        odd_ch = ''
        for k, v in cnt.items():
            if v % 2:
                odd += 1
                odd_ch = k
                cnt[k] -= 1

        if odd > 1:
            return ""

        left = []
        res = ""
        temp = cnt.copy()
        def dfs(i, is_bigger):
            if i == n // 2:
                nonlocal res
                pd = ''.join(left) + odd_ch + ''.join(left[::-1])
                if pd > target and pd > res:
                    res = pd
                    return True
                return False

            choices = sorted(temp.keys())
            for ch in choices:
                if not is_bigger and ch < target[i]:
                    continue
                if temp[ch] == 0:
                    continue

                temp[ch] -= 2
                left.append(ch)
                new_is_bigger = is_bigger or (ch > target[i])

                if dfs(i + 1, new_is_bigger):
                    return True
                
                temp[ch] += 2
                left.pop()

            return False
        
        dfs(0, False)
        return res if res else ""   # 31ms
    

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        odd = 0
        odd_ch = ''
        for k, v in cnt.items():
            if v % 2:
                odd += 1
                odd_ch = k
                cnt[k] -= 1

        if odd > 1:
            return ""

        left = []
        res = ""
        choices = sorted(cnt.keys())

        def dfs(i, is_bigger):
            if i == n // 2:
                nonlocal res
                pd = ''.join(left) + odd_ch + ''.join(left[::-1])
                if pd > target and pd > res:
                    res = pd
                    return True
                return False

            for ch in choices:
                if not is_bigger and ch < target[i]:    
                    # 这里要注意一下: 如果前面已经存在字符比对位字符大
                    # 那么 ch 就可以小于他对位字符
                    continue
                if cnt[ch] == 0:
                    continue

                cnt[ch] -= 2
                left.append(ch)
                new_is_bigger = is_bigger or (ch > target[i])

                if dfs(i + 1, new_is_bigger):
                    return True
                
                cnt[ch] += 2
                left.pop()

            return False
        
        dfs(0, False)
        return res if res else ""   # 19ms
    

class Solution:
    # 灵神
    # 倒序贪心
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        left = Counter(s)

        mid_ch = ''
        for ch, c in left.items():
            if c % 2 == 0:
                continue
            # s 不能有超过一个字母出现奇数次
            if mid_ch:
                return ""
            # 记录填在正中间的字母
            mid_ch = ch
            left[ch] -= 1

        n = len(s)
        ans = list(target)
        # 先假设答案左半与 t 的左半（不含正中间）相同
        for i, b in enumerate(target[:n // 2]):
            left[b] -= 2
            ans[-1 - i] = b  # 把 target 左半翻转到右半
        # 正中间只能填那个出现奇数次的字母
        if mid_ch:
            ans[n // 2] = mid_ch

        neg, left_max = 0, ''
        for c, cnt in left.items():
            if cnt < 0:
                neg += 1  # 统计 left 中的负数个数
            elif cnt > 0:
                left_max = max(left_max, c)  # 剩余可用字母的最大值

        # 特殊情况：把 target 左半翻转到右半，能否比 target 大？
        if neg == 0 and (t := ''.join(ans)) > target:
            return t

        for i in range(n // 2 - 1, -1, -1):
            b = target[i]
            left[b] += 2  # 撤销消耗

            if left[b] == 0:
                neg -= 1
            elif left[b] == 2:
                left_max = max(left_max, b)

            # left 有负数 or 没有大于 target[i] 的字母
            if neg > 0 or left_max <= b:
                continue

            # 找到答案（下面的循环在整个算法中只会跑一次）
            j = ord(b) - ord('a') + 1
            while left[ascii_lowercase[j]] == 0:
                j += 1

            # 把 target[i] 和 target[n-1-i] 增大到 ch
            ch = ascii_lowercase[j]
            left[ch] -= 2
            ans[i] = ans[-1 - i] = ch
            right = ans[-1 - i:]
            del ans[i + 1:]

            # 中间的空位可以随便填
            t = []
            for ch in ascii_lowercase:
                t.extend(ch * (left[ch] // 2))

            ans += t
            if mid_ch:
                ans.append(mid_ch)
            ans += t[::-1]
            ans += right

            return ''.join(ans)
        return ""   # 11ms