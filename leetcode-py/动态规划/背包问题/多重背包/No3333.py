# class Solution:
#     def possibleStringCount(self, word: str, k: int) -> int:
#         n = len(word)
#         if n < k: return 0

#         MOD = 10 ** 9 + 7

#         # 先统计一下有至少有多少个字母，每个字母有多少个
#         cnts = []   # dp 中的字母
#         count = 0
#         for i in range(n):
#             count += 1
#             if i == n - 1 or word[i] != word[i + 1]:
#                 if count > 1: # == 1 时说明这个必选，不需要参与dp
#                     if k > 0:
#                         cnts.append(count - 1)


from functools import cache
from itertools import accumulate


class Solution:
    # 递归
    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        if n < k:
            return 0

        MOD = 10 ** 9 + 7
        groups = []
        cnt = 0
        for i in range(n):
            cnt += 1
            if i == n - 1 or word[i] != word[i + 1]:
                groups.append(cnt)
                cnt = 0

        m = len(groups)

        @cache
        def dfs(i: int, cur_len: int):
            if i == m:
                return 1 if cur_len >= k else 0
            
            count = groups[i]
            res = 0
            for new_len in range(1, count + 1):
                res += dfs(i + 1, cur_len + new_len)

            return res
        
        dfs.cache_clear()
        return dfs(0, 0) % MOD  # 不加cache超时， 加了爆内存


class Solution:
    # dp
    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        if n < k:
            return 0

        MOD = 10 ** 9 + 7
        groups = []
        cnt = 0
        for i in range(n):
            cnt += 1
            if i == n - 1 or word[i] != word[i + 1]:
                groups.append(cnt)
                cnt = 0

        m = len(groups)

        # 初始化DP数组
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1  # 基础情况：当没有分组时，长度为0的情况有1种

        for i in range(1, m + 1):
            count = groups[i - 1]
            for cur_len in range(n + 1):
                for pre_len in range(1, count + 1):
                    if cur_len >= pre_len:
                        dp[i][cur_len] = (dp[i][cur_len] + dp[i - 1][cur_len - pre_len]) % MOD
                    else:
                        break

        return sum(dp[m][cur_len] for cur_len in range(k, n + 1)) % MOD # 超时 比上面好一个用例
    

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        if n < k:
            return 0

        MOD = 10 ** 9 + 7
        groups = []
        cnt = 0
        for i in range(n):
            cnt += 1
            if i == n - 1 or word[i] != word[i + 1]:
                groups.append(cnt)
                cnt = 0

        m = len(groups)

        # 初始化DP数组
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(n + 1):
            dp[0][i] = 1  # 基础情况：当没有分组时，长度为0的情况有1种 即dp[0][0] = 1 并计算前缀和

        for i in range(1, m + 1):
            count = groups[i - 1]

            for cur_len in range(1,n + 1):
                MN = max(cur_len - count, 0)
                dp[i][cur_len] = (dp[i][cur_len] + (dp[i - 1][cur_len - 1] - dp[i - 1][MN])) % MOD

            for j in range(1,n + 1):
                dp[i][j] = (dp[i][j] + dp[i][j - 1]) % MOD

        return sum(dp[m][cur_len] for cur_len in range(k, n + 1)) % MOD # 这一段前缀和代码存在问题
    


class Solution:
    # 前缀和优化
    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        if n < k:
            return 0

        MOD = 10 ** 9 + 7
        groups = []
        cnt = 0
        for i in range(n):
            cnt += 1
            if i == n - 1 or word[i] != word[i + 1]:
                groups.append(cnt)
                cnt = 0

        m = len(groups)

        # 初始化DP数组
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1  # 基础情况：当没有分组时，长度为0的情况有1种

        # 初始化前缀和数组
        prefix = [0] * (n + 2)
        prefix[1] = 1
        for j in range(1, n + 2):
            prefix[j] += prefix[j - 1]

        for i in range(1, m + 1):
            count = groups[i - 1]

            for cur_len in range(1,n + 1):
                MN = max(cur_len - count, 0)
                dp[i][cur_len] = (dp[i][cur_len] + (prefix[cur_len - 1 + 1] - prefix[MN])) % MOD

            prefix[1:] = dp[i][:]
            for j in range(1, n + 2):
                prefix[j] += prefix[j - 1]

        return sum(dp[m][cur_len] for cur_len in range(k, n + 1)) % MOD # 比上面那个好两个用例
    

# 已经红温 ！！！

class Solution:
    # 正难则反 计算不考虑 k 的全部的个数 减去 长度小于 k 的原串个数
    # 灵神
    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        if n < k:  # 无法满足要求
            return 0

        MOD = 1_000_000_007
        cnts = []
        ans = 1
        cnt = 0
        for i in range(n):
            cnt += 1
            if i == n - 1 or word[i] != word[i + 1]:
                # 如果 cnt = 1，这组字符串必选，无需参与计算
                if cnt > 1:
                    if k > 0:
                        cnts.append(cnt - 1)
                    ans = ans * cnt % MOD
                k -= 1  # 注意这里把 k 减小了
                cnt = 0

        if k <= 0:
            return ans

        f = [[0] * k for _ in range(len(cnts) + 1)]
        f[0] = [1] * k
        for i, c in enumerate(cnts):
            # 计算 f[i] 的前缀和数组 s
            s = list(accumulate(f[i], initial=0))
            # 计算子数组和
            for j in range(k):
                f[i + 1][j] = (s[j + 1] - s[max(j - c, 0)]) % MOD
        return (ans - f[-1][-1]) % MOD  # 2198ms


# leetcode 大佬 白
# https://leetcode.cn/problems/find-the-original-typed-string-ii/solutions/2966981/sheng-cheng-han-shu-jie-fa-oklogk-by-vcl-42eq/
# 1079ms
import numpy as np

def polymul(lhs, rhs, MOD):
    n_lhs = len(lhs)
    n_rhs = len(rhs)
    n = n_lhs + n_rhs - 1
    
    if n_lhs <= 64:
        rhs = rhs.astype(np.uint64)
        total = np.zeros(n, dtype = np.uint64)
        for i, e in enumerate(lhs):
            total[i: i + n_rhs] += np.uint64(e) * rhs % MOD
        return total % MOD
    
    elif n_rhs <= 64:
        lhs = lhs.astype(np.uint64)
        total = np.zeros(n, dtype = np.uint64)
        for i, e in enumerate(rhs):
            total[i: i + n_lhs] += np.uint64(e) * lhs % MOD
        return total % MOD
    
    else:
        p = (lhs & 65535) + 1j * (lhs >> 16)
        f_p = np.fft.fft(p, n)
        f_cp = np.conj(np.append(f_p[0:1], f_p[-1:0:-1]))

        q = (rhs & 65535) + 1j * (rhs >> 16)
        f_q = np.fft.fft(q, n)
        
        pq = np.fft.ifft(f_p * f_q, n)
        cpq = np.fft.ifft(f_cp * f_q, n)

        s = np.round(0.5 * (pq + cpq))
        d = np.round(-0.5j * (pq - cpq))

        ans00 = s.real.astype(np.uint64)
        ans01 = s.imag.astype(np.uint64)
        ans10 = d.real.astype(np.uint64)
        ans11 = d.imag.astype(np.uint64)
        
        return (ans00 % MOD + (((ans01 + ans10) % MOD) << 16) + ((ans11 % MOD) << 32)) % MOD

def polyninv(x, n, MOD):
    y = np.array([pow(MOD - int(x[0]), MOD - 2, MOD)], dtype = np.uint64)
    l = 1
    while l < n:
        l = min(2 * l, n)
        t = polymul(x[:l], y, MOD)[:l]
        t[0] += 2
        y = polymul(t, y, MOD)[:l]
    return y

def polyinv(x, n, MOD):
    return polyninv(MOD - x, n, MOD)

def polyder(x, MOD):
    return x[1:] * np.arange(1, len(x), dtype = np.uint64) % MOD

def polyint(x, INV, MOD):
    return np.append([np.uint64(0)], x * INV[:len(x)] % MOD)

def polylog(x, n, INV, MOD):
    return polyint(polymul(polyder(x[:n + 1], MOD), polyinv(x, n, MOD), MOD)[:n - 1], INV, MOD)

def polyexp(x, n, INV, MOD):
    y = np.array([1, 0], dtype = np.uint64)
    l = 1
    while l < n:
        l = min(2 * l, n)
        t = (MOD - polylog(y, l, INV, MOD))
        t[:len(x)] += x[:l]
        t[0] += 1
        y = polymul(t, y, MOD)[:l]
    return y

MOD = 1000000007
K = 2000
INV = [1] * (K + 1)
for i in range(2, K + 1):
    INV[i] = (MOD - MOD // i) * INV[MOD % i] % MOD
NP_INV = np.array(INV[1:], dtype = np.uint64)

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        log_f = [0] * k
        pre_ch = word[0]
        l = 0
        n = 1
        total = 1
        for ch in word:
            if ch == pre_ch:
                l += 1
            else:
                n += 1
                if l < k:
                    log_f[l] += 1
                total = total * l % MOD
                pre_ch = ch
                l = 1
        total = total * l % MOD
        if k <= n:
            return total
        if l < k:
            log_f[l] += 1
        for i in range(k - n - 1, 0, -1):
            if log_f[i] > 0:
                c = log_f[i]
                log_f[i] = 0
                for j in range(1, (k - n - 1) // i + 1):
                    log_f[i * j] -= c * INV[j]
        for i in range(1, k - n):
            log_f[i] = (log_f[i] + n * INV[i]) % MOD
        f = polyexp(np.array(log_f[:k - n], dtype = np.uint64), k - n, NP_INV, MOD)
        return (total - int(np.sum(f))) % MOD