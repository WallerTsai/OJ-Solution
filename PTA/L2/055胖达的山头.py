import sys
# sys.setrecursionlimit(1_000_000_000)

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())

# data = sys.stdin.read().strip().split()
# it = iter(data)

out = sys.stdout.write 

def f(li: list):
    return li[0] * 60 * 60 + li[1] * 60 + li[2]

n = ii()
li = [0] * (24 * 60 * 60 + 1)

for _ in range(n):
    s, e = input().split()
    s = list(map(int, s.split(':')))
    e = list(map(int, e.split(':')))

    left = f(s)
    right = f(e)
    li[left] += 1
    li[right + 1] -= 1

ans = cur = 0
for x in li:
    cur += x
    if cur > ans:
        ans = cur
out(str(ans))
