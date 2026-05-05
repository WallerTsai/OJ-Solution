from collections import Counter
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
        n = ii()
        li = lii()
        m = len(li)
        cnt = Counter(li)

        ans = cur = 0
        for i, (k, v) in enumerate(sorted(cnt.items(), key=lambda x: x[1], reverse=True), start=1):
            cur += v
            K = cur // i * i
            ans = max(ans, K)
        
        out(str(ans) + "\n")

if __name__ == "__main__":
    main()