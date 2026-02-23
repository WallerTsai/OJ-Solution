from math import inf
import sys

sys.setrecursionlimit(200_000)

# f佬的IO模板
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())
out = sys.stdout.write

if __name__ == '__main__':
    n = ii()
    li = lii()
    ans = -inf
    cur_sum = min_sum = 0
    for num in li:
        cur_sum += num
        ans = max(ans, cur_sum - min_sum)
        min_sum = min(min_sum, cur_sum)
    out(str(ans))