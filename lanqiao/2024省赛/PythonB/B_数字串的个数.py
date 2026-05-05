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
    MOD = 10 ** 9 + 7
    ans = pow(9, 10_000, MOD) - pow(8, 10_000, MOD) - pow(8, 10_000, MOD) + pow(7, 10_000, MOD)
    out(str(ans % MOD))



if __name__ == "__main__":
    main()