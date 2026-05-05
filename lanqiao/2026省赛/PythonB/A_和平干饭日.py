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
    cur = ''
    ans = 0
    for i in range(1, 2026 + 1):
        cur += str(i)
        if int(cur) % 26 == 0:
            ans += 1
    out(str(ans))


if __name__ == "__main__":
    main()