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
    n, m = mii()
    data = sys.stdin.read().strip().split()
    it = iter(data)
    mp1 = defaultdict(int)
    mp2 = defaultdict(int)
    ans = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            x = next(it)

            ans += mp1[(x, i - j)]
            mp1[(x, i - j)] += 1
            ans += mp2[(x, i + j)]
            mp2[(x, i + j)] += 1

    out(str(ans * 2))


if __name__ == "__main__":
    main()



import os
import sys
from collections import Counter

n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

def count(a:list):
  ans = 0
  # k = i - j + m
  for k in range(1,n + m):
    maxj = min(n - 1 - k + m, m - 1)
    minj = max(m -k,0)
    c = Counter()
    for j in range(minj, maxj+1):
      c[a[k + j - m][j]] += 1
    for v in c.values():
      ans += v * (v - 1)
  return ans

if __name__ == "__main__":
  b = [a[i][::-1] for i in range(n)]
  print(count(a) + count(b))