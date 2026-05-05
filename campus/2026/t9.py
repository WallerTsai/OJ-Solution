from collections import defaultdict
import os
import sys
sys.setrecursionlimit(100_000)

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())

# data = sys.stdin.read().strip().split()
# it = iter(data)

out = sys.stdout.write       


def main():
    n, m = mii()
    li = []
    for _ in range(m):
        temp = lii()
        li.append(set(temp[1:]))

    g = defaultdict(list)
    for i in range(m):
        for j in range(i + 1, m):
            if not li[i].isdisjoint(li[j]):
                g[i].append(j)
                g[j].append(i)

    ans = 0
    confl = [0] * m
    def dfs(i: int, cur: int):
        nonlocal ans
        if cur + m - i < ans:
            return
        
        if i == m:
            ans = max(ans, cur)
            return
        
        # 选
        if not confl[i]:
            for v in g[i]:
                confl[v] += 1
            dfs(i + 1, cur + 1)
            for v in g[i]:
                confl[v] -= 1
    
        # 不选
        dfs(i + 1, cur)

    dfs(0, 0)
    out(str(ans))

if __name__ == "__main__":
    # a = set([1, 2])
    # b = set([3, 4])
    # print(a.isdisjoint(b))
    main()