from collections import defaultdict
from heapq import heappop, heappush
from math import inf
import sys
# sys.setrecursionlimit(1_000_000)

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())

# data = sys.stdin.read().strip().split()
# it = iter(data)

out = sys.stdout.write     

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)

    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    adj = defaultdict(list)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        s = int(next(it))
        e = int(next(it))
        adj[u].append((v, w, s, e))
        adj[v].append((u, w, s, e))

    hq = [(0, 1, 0)]    # （耗时， 节点， 技能次数）
    # dist[i][j] 表示到达结点 i，且使用了 j 次技能的最短时间
    dist = [[inf] * (k + 1) for _ in range(n + 1)]
    dist[1][0] = 0
    while hq:
        t, u, j = heappop(hq)
        if t > dist[u][j]:
            continue

        if u == n:
            print(t)
            return
        
        for v, w, s, e in adj[u]:
            # 不使用技能
            if t <= e:
                start = t if t >= s else s
                end = start + w
                if end < dist[v][j]:
                    dist[v][j] = end
                    heappush(hq, (end, v, j))
            # 能够使用技能
            if j < k:
                end = t + w
                if end < dist[v][j + 1]:
                    dist[v][j + 1] = end
                    heappush(hq, (end, v, j + 1))

    print(-1)
    return -1
        
if __name__ == "__main__":
    main()