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

    g = defaultdict(int)
    for i, v in enumerate(li, start=1):
        g[i] = v

    ans = 0
    visited = set()
    for i in range(1, n + 1):
        if i in visited:
            continue

        t = 0
        cur = i
        while cur not in visited:
            visited.add(cur)
            cur = g[cur]
            t += 1

        ans += t - 1

    out(str(ans))
        
if __name__ == "__main__":
    main()