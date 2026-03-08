import sys
# sys.setrecursionlimit(1_000_000_000)

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())

# data = sys.stdin.read().strip().split()
# it = iter(data)

out = sys.stdout.write  

T, p, t = lii()
if T > 35 and t >= 33:
    if p == 0:
        print("Shi Nei")
    else:
        print("Bu Tie")
    print(T)
else:
    if p == 0:
        print("Shu Shi")
    else:
        print("Bu Re")
    print(t)


