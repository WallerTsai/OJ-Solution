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
    target = {"lqb", "lbq", "qlb", "qbl", "blq", "bql"}
    s = input()
    n = len(s)
    i = 2
    ans = 0
    while i < n:
        t = s[i - 2: i + 1]
        if t in target:
            ans += 1
            i += 3
        else:
            i += 1
    out(str(ans))
        
if __name__ == "__main__":
    main()
