from math import isqrt
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
        if n <= 4:
            print(4)
            continue
        sqrt_n = isqrt(n)
        if pow(sqrt_n, 2) == n:
            print(n)
            continue
        print(sqrt_n * ((n - 1) // sqrt_n + 1)) # 错误


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        
    return True

def main():
    t = ii()
    for _ in range(t):
        n = ii()
        if n <= 4:
            print(4)
            continue

        if is_prime(n):
            print(n + 1)
        else:
            print(n)


if __name__ == "__main__":
    main()