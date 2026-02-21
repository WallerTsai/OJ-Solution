from collections import deque
from math import gcd, inf


class Solution:
    # 枚举
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        ans = s
        n = len(s)
        s = list(s)

        for i in range(n):
            s = s[-b:] + s[:-b]
            for j in range(10):
                for k in range(1, n, 2):
                    s[k] = str((int(s[k]) + a) % 10)
                if b % 2 == 1:
                    for j in range(10):
                        for k in range(0, n, 2):
                            s[k] = str((int(s[k]) + a) % 10)
                        t = ''.join(s)
                        if ans > t:
                            ans = t
                else:
                    t = ''.join(s)
                    if ans > t:
                        ans = t
        return ans

class Solution:
    # 枚举 + 剪枝
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        ans = s
        n = len(s)
        s = list(s)
        s_set = set()
        for _ in range(n):
            s = s[-b:] + s[:-b]
            if ''.join(s) in s_set:
                break
            for _ in range(10):
                for k in range(1, n, 2):
                    s[k] = str((int(s[k]) + a) % 10)
                t = ''.join(s)
                if t in s_set:
                    break
                if b % 2 == 1:
                    for _ in range(10):
                        for k in range(0, n, 2):
                            s[k] = str((int(s[k]) + a) % 10)

                        t = ''.join(s)
                        if t in s_set:
                            break
                        else:
                            s_set.add(t)
                        if ans > t:
                            ans = t
                else:
                    s_set.add(t)
                    if ans > t:
                        ans = t
        return ans


class Solution:
    # bfs
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        q = deque([s])
        visited = {s}
        ans = s
        while q:
            s = q.popleft()
            if ans > s:
                ans = s
            t1 = ''.join([str((int(c) + a) % 10) if i & 1 else c for i, c in enumerate(s)])
            t2 = s[-b:] + s[:-b]
            for t in (t1, t2):
                if t not in visited:
                    visited.add(t)
                    q.append(t)
        return ans
    

class Solution:
    # 灵神
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        s = list(map(int, s))
        n = len(s)
        step = gcd(b, n)
        g = gcd(a, 10)
        ans = [inf]

        def modify(start: int) -> None:
            ch = t[start]  # 最靠前的数字，越小越好
            # ch 可以变成的最小值为 ch%g
            # 例如 ch=5，g=2，那么 ch+2+2+2（模 10）后变成 1，不可能变得更小
            # 从 ch 到 ch%g，需要增加 inc（循环中会 %10 保证结果在 [0,9] 中）
            inc = ch % g - ch
            if inc:  # 优化：inc 为 0 时，t[j] 不变，无需执行 for 循环
                for j in range(start, n, 2):
                    t[j] = (t[j] + inc) % 10

        for i in range(0, n, step):      
            t = s[i:] + s[:i]  # 轮转
            modify(1)  # 累加操作（所有奇数下标）
            if step % 2:  # 能对偶数下标执行累加操作
                modify(0)  # 累加操作（所有偶数下标）
            ans = min(ans, t)

        return ''.join(map(str, ans))