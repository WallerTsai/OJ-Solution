# 数学 + P1226

import math
import sys

sys.setrecursionlimit(200_000)

# f佬的IO模板
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())
out = sys.stdout.write

if __name__ == "__main__":
    p = ii()
    l = int(p * math.log10(2)) + 1
    out(str(l) + '\n')

    num = pow(2, p, 10 ** 500) - 1
    ans = str(num).zfill(500)
    for i in range(0, 500, 50):
        out(ans[i: i + 50] + '\n')

