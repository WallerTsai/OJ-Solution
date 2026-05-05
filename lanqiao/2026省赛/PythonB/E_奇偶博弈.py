import sys
sys.setrecursionlimit(100_000)
sys.set_int_max_str_digits(10_000_000)

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
        print("QL"[li.count(1) % 2])


if __name__ == "__main__":
    main()