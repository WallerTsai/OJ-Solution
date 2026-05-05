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

def sum_base(a: int, b: int):
    res = 0
    while a > 0:
        res += a % b
        a //= b
    return res


def main():
    ans = 0
    for i in range(1, 2024):
        if sum_base(i, 2) == sum_base(i, 4):
            ans += 1
    out(str(ans))


if __name__ == "__main__":
    main()