from collections import Counter
from functools import lru_cache
import sys
# sys.setrecursionlimit(1_000_000)

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())

# data = sys.stdin.read().strip().split()
# it = iter(data)

out = sys.stdout.write      

@lru_cache()
def A(n, m):
    if m > n or m < 0:
        return 0
    res = 1
    for i in range(m):
        res *= n - i
    return res

def main():
    n = ii()
    li = lii()
    cnt = Counter(li)
    MOD = 10 ** 9 + 7
    res = 0
    for i in cnt.keys():
        for j in cnt.keys():
            if i == j:
                if cnt[i] < 4:
                    continue
                res = (res + A(cnt[i], 4)) % MOD
            else:
                if cnt[i] < 2 or cnt[j] < 2:
                    continue
                res = (res + A(cnt[i], 2) * A(cnt[j], 2)) % MOD
    print(res)
    return

if __name__ == "__main__":
    main()
