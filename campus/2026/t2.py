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
    s = input()
    ans = cur = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cur += 1
            ans = max(ans, cur)
        else:
            cur = 1
    out(str(ans))


if __name__ == "__main__":
    main()