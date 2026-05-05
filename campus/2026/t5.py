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
        n, a, b = lii()

        cnta = a.bit_count()
        cntb = b.bit_count()

        k = cnta + cntb
        left = cnta + cntb - n

        if left <= 0:
            res = ((1 << k) - 1) << (n - k)
        else:
            res = ((1 << (n - left)) - 1) << (left)

        out(str(res) + "\n")

if __name__ == "__main__":
    main()