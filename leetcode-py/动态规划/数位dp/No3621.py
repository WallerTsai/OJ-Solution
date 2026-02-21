from collections import defaultdict
from functools import cache

cnt = defaultdict(int)
@cache
def dfs(i: int):
    if i == 1:
        return 0
    depth = 1 + dfs(i.bit_count())
    return depth
for i in range(1, 10 ** 6):
    m = dfs(i)
    cnt[m] += 1

class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        @cache
        def dfs(i: int):
            if i == 1:
                return 0
            depth = 1 + dfs(i.bit_count())
            return depth
        
        ans = 0

        if n < 10 ** 6:
            for i in range(1, n + 1):
                if dfs(i) == k:
                    ans += 1
            return ans
        
        for i in range(10 ** 6, n + 1):
            if dfs(i) == k:
                ans += 1
        dfs.cache_clear()
        return ans + cnt[k] # 上面方法爆内存
    

class Solution:
    # 数位dp 灵神 暂时不理解
    def popcountDepth(self, n: int, k: int) -> int:
        if k == 0:
            return 1
        
        s = list(map(int, bin(n)[2:]))
        m = len(s)
        if k == 1:
            return m - 1
        
        @cache
        def dfs(i: int, left1: int, is_limit: bool):
            if i == m:
                return 0 if left1 else 1
            
            up = s[i] if is_limit else 1
            res = 0
            for d in range(min(up, left1) + 1):
                res += dfs(i + 1, left1 - d, is_limit and d == up)
            return res

        ans = 0
        f = [0] * (m + 1)
        for i in range(1, m + 1):
            f[i] = f[i.bit_count()] + 1
            if f[i] == k:
                ans += dfs(0, i, True)

        return ans
    
    
# 执行一遍后, popcount不超过50位的1
cnt = [0]
# 预处理，x => 1 要走多少次
for x in range(1,51):
    t = 0
    while x != 1:
        x = x.bit_count()
        t += 1
    cnt.append(t)
class Solution:
    # 数位dp
    def popcountDepth(self, n: int, k: int) -> int:
        if k == 0:
            return 1
        
        s = list(map(int, bin(n)[2:]))
        m = len(s)
        if k == 1:
            return m - 1
        
        @cache
        def dfs(i: int, left1: int, is_limit: bool):
            if i == m:
                return 0 if left1 else 1
            
            up = s[i] if is_limit else 1
            res = 0
            for d in range(min(up, left1) + 1):
                res += dfs(i + 1, left1 - d, is_limit and d == up)
            return res

        ans = 0
        for t in range(2,51):
            if cnt[t] + 1 == k:
                ans += dfs(0,t,True)

        dfs.cache_clear()
        return ans


class Solution:
    # 灵神
    def popcountDepth(self, n: int, k: int) -> int:
        if k == 0:
            return 1

        # 注：也可以不转成字符串，下面 dfs 用位运算取出 n 的第 i 位
        # 但转成字符串的通用性更好
        s = list(map(int, bin(n)[2:]))
        m = len(s)
        if k == 1:
            return m - 1

        @cache
        def dfs(i: int, left1: int, is_limit: bool) -> int:
            if i == m:
                return 0 if left1 else 1
            up = s[i] if is_limit else 1
            res = 0
            for d in range(min(up, left1) + 1):
                res += dfs(i + 1, left1 - d, is_limit and d == up)
            return res

        ans = 0
        f = [0] * (m + 1)
        for i in range(1, m + 1):
            f[i] = f[i.bit_count()] + 1
            if f[i] == k:
                # 计算有多少个二进制数恰好有 i 个 1
                ans += dfs(0, i, True)
        return ans