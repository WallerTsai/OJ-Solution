from collections import defaultdict


class Solution:
    def longestBalanced(self, s: str) -> int:
        cnt = [0] * 3
        hash_map = defaultdict(int)
        ans = 0
        for i, ch in enumerate(s):
            cnt[ord(ch) - ord('a')] += 1
            hash_map[tuple(cnt)] = i

            if len(set([x for x in cnt if x != 0])) == 1:
                ans = i + 1
                continue

            elif len([x for x in cnt if x != 0]) == 2:
                left = i
                while s[left] == ch:
                    left -= 1
                ans = max(ans, i - left)
                continue

            MN = min(cnt)
            d1, d2, d3 = cnt[0] - MN, cnt[1] - MN, cnt[2] - MN
            for k in range(MN):
                x1, x2, x3 = k + d1, k + d2, k + d3
                if (x1, x2, x3) in hash_map:
                    ans = max(ans, i - hash_map[(x1, x2, x3)])
                    break

        return ans  # 错误

class Solution:
    def longestBalanced(self, s: str) -> int:
        cnt = [0] * 3
        hash_map = defaultdict(int)
        hash_map[(0, 0, 0)] == -1
        ans = 0
        for i, ch in enumerate(s):
            cnt[ord(ch) - ord('a')] += 1
            hash_map[tuple(cnt)] = i

            non_zero = [x for x in cnt if x > 0]
            if non_zero and all(x == non_zero[0] for x in non_zero):
                ans = i + 1

            # 只保留一种
            left = i
            while left >= 0 and s[left] == ch:
                left -= 1
            ans = max(ans, i - left)

            # 保留两种
            for a, b in (0, 1), (0, 2), (1, 2):
                if cnt[a] != cnt[b]:
                    continue
                temp = cnt.copy()
                temp[a] = 0
                temp[b] = 0
                if tuple(temp) in hash_map:
                    ans = max(ans, i - hash_map[tuple(temp)])

            MN = min(cnt)
            d1, d2, d3 = cnt[0] - MN, cnt[1] - MN, cnt[2] - MN
            for k in range(MN):
                x1, x2, x3 = k + d1, k + d2, k + d3
                if (x1, x2, x3) in hash_map:
                    ans = max(ans, i - hash_map[(x1, x2, x3)])
                    break

            hash_map[tuple(cnt)] = i

        return ans  # 错误
    

class Solution:
    #  分类讨论
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 1

        # 一种字母
        pre = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                pre += 1
            if s[i] != s[i - 1] or i == n - 1:
                ans = max(ans, pre)
                pre = 1

        # 两种字母
        # LC No.525
        for x, y in (('a','b'), ('a','c'), ('b','c')):
            diff = 0
            cnt = {0: -1}
            for i, ch in enumerate(s):
                if ch == x:
                    diff += 1
                elif ch == y:
                    diff -= 1
                else:
                    diff = 0
                    cnt = {0: i}
                    continue

                if diff in cnt:
                    ans = max(ans, i - cnt[diff])
                else:
                    cnt[diff] = i

        # 三种字母
        pos = {(0, 0): -1} # 这里考虑记录 (count_a - count_b, count_b - count_c)
        cnt_ch = defaultdict(int)
        for i, ch in enumerate(s):
            cnt_ch[ch] += 1
            p = (cnt_ch['a'] - cnt_ch['b'], cnt_ch['b'] - cnt_ch['c'])
            if p in pos:
                ans = max(ans, i - pos[p])
            else:
                pos[p] = i

        return ans  # 1414ms


fun = Solution()
fun.longestBalanced("abbac")



class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0

        # 一种字母
        i = 0
        while i < n:
            start = i
            i += 1
            while i < n and s[i] == s[i - 1]:
                i += 1
            ans = max(ans, i - start)

        # 两种字母
        def f(x, y):
            res = diff = 0
            cnt = {0: -1}
            for i, ch in enumerate(s):
                if ch == x:
                    diff += 1
                elif ch == y:
                    diff -= 1
                else:
                    diff = 0
                    cnt = {0: i}
                    continue
                
                if diff in cnt:
                    res = max(res, i - cnt[diff])
                else:
                    cnt[diff] = i
            return res
        
        ans = max(ans, f('a', 'b'), f('a', 'c'), f('b', 'c'))

        # 三种字母
        pos = {(0, 0): -1}
        count = defaultdict(int)
        for i, ch in enumerate(s):
            count[ch] += 1
            p = (count['a'] - count['b'], count['b'] - count['c'])
            if p in pos:
                ans = max(ans, i - pos[p])
            else:
                pos[p] = i

        return ans  # 971ms


