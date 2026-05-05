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
    w, h, l = mii()
    for _ in range(h):
        out('Q' * w + '\n')
    for _ in range(w):
        out('Q' * (w + l) + '\n')
        
if __name__ == "__main__":
    main()
    