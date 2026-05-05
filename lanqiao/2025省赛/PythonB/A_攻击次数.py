import sys
# sys.setrecursionlimit(1_000_000_000)

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())

# data = sys.stdin.read().strip().split()
# it = iter(data)

out = sys.stdout.write         


def main():
    cur = 2025
    for i in range(1, 405):
        cur -= 5

        if i & 1:
            cur -= 15
        else:
            cur -= 2

        if i % 3 == 1:
            cur -= 2
        elif i % 3 == 2:
            cur -= 10
        else:
            cur -= 7

        if cur <= 0:
            out(str(i))
            return
        
if __name__ == "__main__":
    main()
    