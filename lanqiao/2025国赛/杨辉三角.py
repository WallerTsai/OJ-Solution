from collections import Counter, defaultdict
from math import comb
import sys
# sys.setrecursionlimit(1_000_000)

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())

# data = sys.stdin.read().strip().split()
# it = iter(data)

out = sys.stdout.write    


def main(): # 超时
    n = ii()
    cnt = defaultdict(int)
    li = [1, 1]
    MIN = 1
    while MIN < n:
        nxt = [1]
        m = len(li)
        for i in range(1, m):
            val = li[i] + li[i - 1]
            nxt.append(val)
            if val <= n:
                cnt[val] += 1
        nxt.append(1)
        MIN = nxt[1]
        li = nxt
    
    cnt2 = Counter(cnt.values())
    for i in sorted(cnt2.keys()):
        v = cnt2[i]
        print(f"{i} {v}")


def main(): # 超时
    n = ii()
    cnt = defaultdict(int)
    for k in range(n, 1, -1):
        i = 1
        l = k + 1
        mid = l // 2
        while i < mid:
            val = comb(k, i)
            if val > n:
                break
            cnt[val] += 2
            i += 1
        if l % 2 == 1:
            val = comb(k, mid)
            if val <= n:
                cnt[val] += 1
    
    cnt2 = Counter(cnt.values())
    for i in sorted(cnt2.keys()):
        v = cnt2[i]
        print(f"{i} {v}")

if __name__ == "__main__":
    main()



# Gemini 过题代码 
# 横看成岭侧成峰

from collections import Counter, defaultdict
import sys
import math

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())

def main():
    n = ii()
    if n < 2:
        return
    
    # 用数组代替 defaultdict 会快很多，n=100,000 占用空间极小
    # 初始化：每个数 x 都在 C(x, 1) 和 C(x, x-1) 出现，基础次数为 2
    # 特例：2 处于 C(2, 1)，是中位数，初始次数为 1
    f = [2] * (n + 1)
    f[2] = 1
    
    k = 2
    while True:
        # 数学终止条件：如果该列最顶端的数（中位数）都超过了 n，直接结束
        if math.comb(2 * k, k) > n:
            break
        
        r = 2 * k
        while True:
            val = math.comb(r, k)
            if val > n:
                break
            
            # 逻辑判定：
            if r == 2 * k:
                f[val] += 1  # 处于中轴线，只多出 1 个
            else:
                f[val] += 2  # 不在中轴线，根据对称性，在右半边对应位置还有一个
            r += 1
        k += 1
    
    # 统计 f(x) 值的分布，x 范围 [2, n]
    cnt2 = Counter(f[2:])
    
    for i in sorted(cnt2.keys()):
        print(f"{i} {cnt2[i]}")

if __name__ == "__main__":
    main()