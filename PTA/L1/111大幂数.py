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
    n = ii()
    for k in range(30, 0, -1):
        cur = 0
        i = 1
        while cur < n:
            cur += pow(i, k)
            i += 1
        if cur == n:
            print(*(f"{j}^{k}" for j in range(1, i)), sep='+')
            return
    print(f"Impossible for {n}.")

if __name__ == "__main__":
    main()
