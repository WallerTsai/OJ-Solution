import sys
# from datetime import *
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
    i = ii()
    for _ in range(i):
        n = ii()
        if n % 3:
            print(n)
        else:
            print(2 * n)


if __name__ == "__main__":
    main()
