from bisect import bisect_left
from collections import defaultdict
from math import inf


class Solution:
    def longestBalanced(self, s: str) -> int:
        cnt0 = s.count('0')
        cnt1 = s.count('1')
        if cnt0 == 0 or cnt1 == 0:
            return 0
        
        pos = defaultdict(list)
        pos[0].append(-1)

        ans = count = 0
        for i, ch in enumerate(s):
            count += 1 if ch == '1' else -1

            for d in (-2, 0, 2):
                t = count - d
                if t in pos:
                    # 如果子串的差值为 2，说明我们需要子串外有 '0'。这就要求子串内部的 '0' 的数量必须严格小于总数 cnt0。
                    # 设子串长度为 L 。因为差值为 2，内部 '0' 的数量为 (L - 2) / 2。
                    # 满足条件：(L - 2) / 2 < cnt0 => L <= 2 *cnt0。
                    limit = inf
                    if d == 2:
                        limit = cnt0 * 2
                    elif d == -2:
                        limit = cnt1 * 2

                    idx = bisect_left(pos[t], i - limit)
                    if idx < len(pos[t]):
                        ans = max(ans, i - pos[t][idx])
            
            pos[count].append(i)

        return ans
    

class Solution:
    # 灵神
    def longestBalanced(self, s: str) -> int:
        total0 = s.count('0')
        total1 = len(s) - total0

        pos = defaultdict(list)
        pos[0] = [-1]  # 见 525 题
        ans = 0
        pre = 0  # 前缀和

        for i, ch in enumerate(s):
            pre += 1 if ch == '1' else -1

            if len(pos[pre]) < 2:
                pos[pre].append(i)

            # 不交换
            ans = max(ans, i - pos[pre][0])

            # 交换子串内的一个 1 和子串外的一个 0
            if pre - 2 in pos:
                p = pos[pre - 2]
                if (i - p[0] - 2) // 2 < total0:
                    ans = max(ans, i - p[0])
                elif len(p) > 1:
                    ans = max(ans, i - p[1])

            # 交换子串内的一个 0 和子串外的一个 1
            if pre + 2 in pos:
                p = pos[pre + 2]
                if (i - p[0] - 2) // 2 < total1:
                    ans = max(ans, i - p[0])
                elif len(p) > 1:
                    ans = max(ans, i - p[1])

        return ans

