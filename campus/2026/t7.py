import os
import sys
# sys.setrecursionlimit(100_000)

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())

# data = sys.stdin.read().strip().split()
# it = iter(data)

out = sys.stdout.write       


def main():
    t = ii()
    for _ in range(t):
        a, b, k = mii()

        cnt1 = 0
        x, y = a, b
        while y // k >= x:
            cnt1 += 1
            y, l = divmod(y, k)
            cnt1 += l
        cnt1 += y - x

        cnt2 = 0
        x, y = a, b
        while x * k <= y:
            cnt2 += 1
            x *= 2
        cnt2 += y - x

        ans = min(cnt1, cnt2)
        out(str(ans) + "\n")


if __name__ == "__main__":
    main()