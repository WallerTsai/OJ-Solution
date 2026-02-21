import json
import sys
import functools
import heapq
from typing import List, Dict, Tuple, Optional
import math
from collections import defaultdict, deque
import os
import random
from itertools import permutations
import bisect
null = None
true = True
false = False
def get_log(*args, **kw):
    pass
class logger:
    info = get_log
    map = get_log
    debug = get_log
TheDevLoger = logger
class CT:
    MOD = (10**9) + 7
    inf = float("inf")
    MX = (10**5) + 1
    min = lambda a, b: a if a < b else b
    max = lambda a, b: a if a > b else b
class MockCf:
    dev = False
    inputs = None
    logger = logger
    def set_logger(self, log):
        self.logger: logger = log
    def set_inputs(self, inputs: str):
        self.inputs = inputs.split("\n")
        return self
    def input(self):
        if os.path.exists("input.txt") and self.inputs is None:
            self.inputs = open("input.txt").read().split("\n")
        if self.dev:
            return self.inputs.pop(0)
        if self.inputs is None:
            self.inputs = []
        self.inputs.append(input())
        return self.inputs[-1]
    def ii(self):
        return [int(v) for v in self.input().split(" ") if v]
    _o = None
    def output(self, s):
        if self._o is None:
            self._o = open("output.txt", "w")
        self._o.write(f"{s}\n")
class MockCg(MockCf):
    name = ""
    def __init__(self):
        super().__init__()
        self.msgs = []
    def log(self, **kw):
        info = dict(inputs=self.inputs)
        info.update(kw)
        print(json.dumps(info), file=sys.stderr)
        self.inputs.clear()
    def output(self, s):
        print(s)
    @classmethod
    def main_py(cls):
        return f"app/yly/envs/cg/{cls.name}/cg.py"
import math
import itertools
from functools import lru_cache
from collections import defaultdict, deque, Counter
@lru_cache(None)
def gcd(v1, v2):
    return gcd(v2, v1 % v2) if v2 > 0 else v1
def pi_float(v):
    if isinstance(v, int):
        return v / 180 * math.pi
    return v
def mul_rect(a, b, mod):
    ans = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[i])):
                ans[i][j] = (ans[i][j] + a[i][k] * b[k][j]) % mod
    return ans
def pow_mul_rect(a, n, f0, mod):
    res = f0
    while n:
        if n & 1:
            res = mul_rect(a, res, mod)
        a = mul_rect(a, a, mod)
        n >>= 1
    return res
def calc_angle(y, x, y1, x1):
    """
    0->2*pi
    """
    a = math.atan2(y1 - y, x1 - x)
    if a < 0:
        return 2 * math.pi + a
    return a
def sin(v):
    return math.sin(pi_float(v))
def cos(v):
    return math.cos(pi_float(v))
def prime_gcds(max_value):
    ret = defaultdict(set)
    for i in range(2, max_value):
        if len(ret[i]):
            continue
        j = i
        while j < max_value:
            ret[j].add(i)
            j += i
        i += 1
    return ret
def mean(array):
    s = sum(array) / len(array)
    return sum([(v - s) ** 2 for v in array])
def decomposition_prime_factors(v):
    ret = dict()
    i = 2
    while i * i <= v:
        while v % i == 0:
            if i not in ret:
                ret[i] = 0
            ret[i] += 1
            v = v // i
        i += 1
    if v > 1:
        ret[v] = 1
    return ret
def prime_flags(max_v):
    ret = [True] * max_v
    ret[0] = False
    ret[1] = False
    for i in range(2, max_v):
        if ret[i] == False:
            continue
        ret[i] = True
        for j in range(i * i, max_v, i):
            ret[j] = False
    return ret
@lru_cache(None)
def stl_2(n, i):
    """
    第二类斯特林数
    n个人 放到i个房间, 不允许房间为空
    """
    if n < i or i == 0:
        return 0
    elif i == n or i == 1:
        return 1
    return stl_2(n - 1, i - 1) + i * stl_2(n - 1, i)
def lucas_mod(n, m, mod):
    """
    lucas定理求组合数的摸
    """
    res = 1
    while n > 0 or m > 0:
        ni = n % mod
        mi = m % mod
        if mi > ni:
            return 0
        res = res * math.comb(ni, mi) % mod
        n //= mod
        m //= mod
    return res
def china_rest_mod(n, m, p):
    """
    中国剩余定理
    """
    mod = 1
    for a in p:
        mod *= a
    ans = 0
    for a in p:
        ans += lucas_mod(n, m, a) * (mod // a)
    return ans % mod
def extended_gcd(a, b):
    if b == 0:
        return 1, 0
    s0, t0 = extended_gcd(b, a % b)
    s = t0
    t = s0 - (a // b) * t0
    return s, t
def sigmoid(x):
    import numpy as np # type: ignore
    return 1.0 / (1 + np.exp(-float(x)))
def atan(x):
    return math.atan(x) * 2 / math.pi
@lru_cache(None)
def jc(n):
    if n <= 2:
        return 2
    return n * jc(n - 1)
MX = 151
C = prime_gcds(MX)
D = prime_flags(MX)
E = dict()
i = 0
for j, v in enumerate(D):
    if v:
        E[j] = i
        i += 1
@functools.lru_cache(None)
def mask(*args):
    ret = 0
    for a in args:
        ret += 1 << E[a]
    return ret
MX = 151
divisors = [[] for _ in range(MX)]
for i in range(1, MX):
    for j in range(i, MX, i):
        divisors[j].append(i)
class Solution(MockCf):
    def countCoprime(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        @functools.lru_cache(None)
        def dfs(i, p):
            self.logger.map(i=i, p=p)
            if i == n:
                return p == 0
            ans = 0
            for j in range(m):
                mk = mask(*C[mat[i][j]])
                if mat[i][j] == 1 or (mk & p) == 0:
                    ans += pow(m, n - i - 1, CT.MOD)
                else:
                    ans += dfs(i + 1, mk & p)
            return ans % CT.MOD
        return (sum(dfs(1, mask(*C[mat[0][i]])) for i in range(m))) % CT.MOD
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD = 1_000_000_007
        @functools.lru_cache(None)  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(i: int, g: int) -> int:
            if i < 0:
                return 1 if g == 1 else 0
            return sum(dfs(i - 1, math.gcd(g, x)) for x in mat[i]) % MOD
        return dfs(len(mat) - 1, 0)
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
    execute = countCoprime

# 来自lc3725的提交