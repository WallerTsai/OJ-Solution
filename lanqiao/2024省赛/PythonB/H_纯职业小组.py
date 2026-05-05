import sys
# from datetime import *
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
    t = ii()
    for _ in range(t):
        n, k = mii()

        di = defaultdict(int)
        for _ in range(n):
            a, b = mii()
            di[a] += b
        
        ans = 0
        cost1 = cost2 = cost3 = 0
        total_g = 0
        for count in di.values():
            ans += min(count, 2)

            g = count // 3
            total_g += g

            if g > 0:
                cost3 += (g - 1)
                last_cost = 1 + count % 3
                if last_cost == 3:
                    cost3 += 1
                elif last_cost == 2:
                    cost2 += 1
                else:
                    cost1 += 1

        if total_g < k:
            out("-1\n")
            continue

        need = k - 1

        n3 = min(need, cost3)
        ans += n3 * 3
        need -= n3

        if need > 0:
            n2 = min(need, cost2)
            ans += n2 * 2
            need -= n2

        if need > 0:
            n1 = min(need, cost1)
            ans += n1
            need -= n1

        out(str(ans + 1) + '\n')



if __name__ == "__main__":
    main()
