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
    n = ii()
    li = lii()
    total = n * (n + 1) // 2
    ans = total - sum(li)
    print(ans)


if __name__ == "__main__":
    main()