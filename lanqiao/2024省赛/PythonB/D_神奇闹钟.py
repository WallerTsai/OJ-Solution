import sys
from datetime import *
from collections import defaultdict
# sys.setrecursionlimit(1_000_000_000)

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())

# data = sys.stdin.read().strip().split()
# it = iter(data)

out = sys.stdout.write         

def func(s: str, delta: int):
    t1 = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
    t0 = datetime(1970, 1, 1)

    now = t1 - t0
    total = now.total_seconds()
    res_s = total - total % delta
    res_t = t0 + timedelta(seconds=res_s)
    
    return res_t.strftime('%Y-%m-%d %H:%M:%S')


def main():
    t = ii()
    for _ in range(t):
        a, b, delta = input().split()
        ans = func(a + " " + b, int(delta) * 60)
        out(ans + '\n')


if __name__ == "__main__":
    main()