
from collections import Counter
from functools import cache
from math import gcd
import math
from typing import List


class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD =  10 ** 9 + 7
        n, m = len(mat), len(mat[0])
        cnt = dict()
        for i, li in enumerate(mat):
            cnt[i] = Counter(li)

        ans = 0
        def dfs(i: int, t: int, res = 1):
            if t == 1:
                nonlocal ans
                ans = (ans + res * pow(m, n - i)) % MOD
                return
            if i == n and t != 1:
                return
            d = cnt[i]
            for k, v in d.items():
                n_t = gcd(t, k)
                dfs(i + 1, n_t, res * v)
        
        for a, b in cnt[0].items():
            dfs(1, a, b)
        
        return ans  # 超时



class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD =  10 ** 9 + 7
        n, m = len(mat), len(mat[0])
        cnt = dict()
        for i, li in enumerate(mat):
            cnt[i] = Counter(li)


        @cache
        def dfs(i: int, t: int):
            if t == 1:
                res = pow(m, n - i) % MOD
                return res
            
            if i == n and t != 1:
                return 0
            
            total = 0
            d = cnt[i]
            for k, v in d.items():
                n_t = gcd(t, k)
                total = (total + v * dfs(i + 1, n_t)) % MOD

            return total
        
        ans = 0
        for a, b in cnt[0].items():
            ans = (ans + b * dfs(1, a)) % MOD
        
        return ans 

class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD =  10 ** 9 + 7
        n, m = len(mat), len(mat[0])
        cnt = dict()
        for i, li in enumerate(mat):
            cnt[i] = Counter(li)


        @cache
        def dfs(i: int, t: int):
            if t == 1:
                res = pow(m, n - i) % MOD
                return res
            
            if i == n and t != 1:
                return 0
            
            total = 0
            d = cnt[i]
            for k, v in d.items():
                n_t = gcd(t, k)
                total = (total + v * dfs(i + 1, n_t)) % MOD

            return total
        
        ans = dfs(0, 0) % MOD
        
        return ans  # 2119ms


# leetcode 大佬
# 理解起来有点小绕
N = 150
is_prime = [True] * (N + 1)
primes = [2]
for i in range(3, math.isqrt(N) + 1, 2):
    if is_prime[i]:
        for j in range(2 * i, N + 1, i):
            is_prime[j] = False

for i in range(3, N + 1, 2):
    if is_prime[i]: primes.append(i)

@cache
def f(x):
    res = 0
    for j, i in enumerate(primes):
        if i > x: break
        if x % i == 0:
            res |= (1 << j)
    return res


MOD = 1000_000_007
class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        @cache
        def dfs(row: int, mask):
            if row == m: return int(mask == 0)
            ans = 0
            for x in mat[row]:
                xx = f(x)
                ans = (ans + dfs(row + 1, mask & xx))% MOD
            return ans
        return dfs(0, (1 << len(primes)) - 1)   # 1432ms


# mipha大佬
mx = 151
# 预处理 求 mx 以内任意两个正整数的gcd
G = [[0] * mx for _ in range(mx)]
for a in range(1,mx):
    for b in range(a+1):
        g = gcd(a,b)
        G[a][b] = G[b][a] = g

class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        '''
        每行选一个数 gcd = 1
        n * m * num = 150 150 150 = 3e6
        dp
        '''
        n = len(mat)
        m = len(mat[0])
        
        # dp[i][num] 到第i行 gcd 为 num 的方案数
        # 滚动数组
        dp = [0] * mx
        mod = int(1e9+7)
        # init 
        for j in range(m):
            num = mat[0][j]
            dp[num] += 1
        
        for i in range(1,n):
            ndp = [0] * mx
            for j in range(m):
                num = mat[i][j]
                for lnum in range(mx):
                    g = G[num][lnum]
                    ndp[g] += dp[lnum]
                    ndp[g] %= mod
            dp = ndp

        return dp[1]
    


class Solution:
    # 灵神
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD = 1_000_000_007

        @cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(i: int, g: int) -> int:
            if i < 0:
                return 1 if g == 1 else 0
            return sum(dfs(i - 1, gcd(g, x)) for x in mat[i]) % MOD

        return dfs(len(mat) - 1, 0)
    


class Solution:
    # 灵神
    # 倍数容斥
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD = 1_000_000_007
        mx = max(map(max, mat))  # 找到矩阵中的最大值，用于确定计算范围
        
        # cnt_gcd[i] 将存储最大公约数恰好为 i 的方案数
        cnt_gcd = [0] * (mx + 1)
        
        # 从大到小枚举所有可能的 gcd 值
        # 原因：我们需要使用容斥原理，较大的 gcd 值会先计算
        for i in range(mx, 0, -1):
            # ============================================
            # 步骤1: 计算所有选择的数都是 i 的倍数的方案数
            # ============================================
            # 这个 res 实际上是 f(i)，即 gcd 是 i 的倍数的方案数
            # 每行选一个 i 的倍数的方案数
            res = 1
            for row in mat:
                cnt = 0  # 统计当前行中 i 的倍数的个数
                for x in row:
                    if x % i == 0:  # x 是 i 的倍数
                        cnt += 1
                if cnt == 0:  # 如果某一行没有 i 的倍数
                    res = 0   # 那么无法从每行都选到 i 的倍数
                    break
                # 乘法原理：每行的选择数相乘
                res = res * cnt % MOD
            
            # ============================================
            # 步骤2: 容斥原理，得到 gcd 恰好为 i 的方案数
            # ============================================
            # 此时 res = f(i) = gcd 是 i 的倍数的方案数
            # 我们需要减去那些 gcd 是 i 的倍数但大于 i 的方案
            # 也就是减去 gcd 为 2i, 3i, 4i... 的方案数
            for j in range(i, mx + 1, i):  # 遍历所有 i 的倍数
                # 减去已经计算过的 gcd 为 j 的方案数
                # 当 j = i 时，cnt_gcd[j] 还是 0（因为从大到小计算）
                # 实际减去的是 j = 2i, 3i, 4i... 的情况
                res -= cnt_gcd[j]
            
            # 存储 gcd 恰好为 i 的方案数
            cnt_gcd[i] = res % MOD
        
        # cnt_gcd[1] 就是最大公约数恰好为 1 的方案数
        return cnt_gcd[1]   # 335ms

# 算法复杂度分析:
# 1. 时间复杂度: O(mx * m * n + mx * log(mx))
#    - 外层循环: mx 次
#    - 内层遍历矩阵: m * n 次
#    - 容斥减法的循环: 调和级数，总复杂度 O(mx * log(mx))
# 2. 空间复杂度: O(mx) 用于存储 cnt_gcd 数组
#
# 核心思路解释:
# 1. 直接计算 gcd=1 的方案数很困难，但计算"所有数都是 k 的倍数"的方案数很容易
# 2. 定义:
#    - f(k) = gcd 是 k 的倍数的方案数（每行选 k 的倍数）
#    - g(k) = gcd 恰好为 k 的方案数（我们想要的结果）
# 3. 容斥关系: g(k) = f(k) - Σ g(j) 对 j = 2k, 3k, 4k...
# 4. 从大到小计算 g(k)，最后 g(1) 就是答案


MX = 151
divisors = [[] for _ in range(MX)]
for i in range(1, MX):
    for j in range(i, MX, i):
        divisors[j].append(i)

class Solution:
    # 灵神
    # 统计因子 + 倍数容斥
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD = 1_000_000_007
        # 预处理每行的因子个数
        divisor_cnt = []
        mx = 0
        for row in mat:
            row_max = max(row)
            mx = max(mx, row_max)
            cnt = [0] * (row_max + 1)
            for x in row:
                for d in divisors[x]:
                    cnt[d] += 1
            divisor_cnt.append(cnt)

        cnt_gcd = [0] * (mx + 1)
        for i in range(mx, 0, -1):
            # 每行选一个 i 的倍数的方案数
            res = 1
            for cnt in divisor_cnt:
                if i >= len(cnt) or cnt[i] == 0:
                    res = 0
                    break
                res = res * cnt[i] % MOD  # 乘法原理

            for j in range(i, mx + 1, i):
                res -= cnt_gcd[j]
            cnt_gcd[i] = res % MOD

        return cnt_gcd[1]
