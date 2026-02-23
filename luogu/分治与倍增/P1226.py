import sys

sys.setrecursionlimit(200_000)

# f佬的IO模板
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())
out = sys.stdout.write

def pow(x: int, n: int, m: int):
    ans = 1 % m
    x = x % m

    while n > 0:
        if n & 1:
            ans = (ans * x) % m
        x = (x * x) % m
        n >>= 1

    return ans

if __name__ == "__main__":
    x, n, m = mii()
    ans = pow(x, n, m)
    out(f"{x}^{n} mod {m}={ans}\n")