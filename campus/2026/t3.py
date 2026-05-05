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
    if n == 1:
        out("1")
        return
    
    if n < 4:
        out("NO SOLUTION")
        return
    
    res = []
    for i in range(2, n + 1, 2):
        res.append(str(i))
    for i in range(1, n + 1, 2):
        res.append(str(i))

    out(' '.join(res))


if __name__ == "__main__":
    main()