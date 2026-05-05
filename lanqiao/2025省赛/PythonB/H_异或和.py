import sys
from collections import defaultdict
# sys.setrecursionlimit(1_000_000_000)

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())

# data = sys.stdin.read().strip().split()
# it = iter(data)

out = sys.stdout.write         


def main():
    n = ii()
    li  = lii()

    ans = 0
    for k in range(20):
        count0 = count1 = 0
        sum_idx_0 = sum_idx_1 = 0

        cur = 0
        for i in range(1, n + 1):
            x = li[i - 1]

            if (x >> k) & 1:
                cur += i * count0 - sum_idx_0
                count1 += 1
                sum_idx_1 += i
            else:
                cur += i * count1 - sum_idx_1
                count0 += 1
                sum_idx_0 += i

        ans += cur << k

    out(str(ans))


if __name__ == "__main__":
    main()