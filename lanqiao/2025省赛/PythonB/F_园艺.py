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
    li  = lii()

    dp = [[1] * n for _ in range(n)]
    ans = 1
    for i in range(1, n):
        for j in range(1, i + 1):
            if li[i - j] < li[i]:
                dp[i][j] += dp[i - j][j]
                ans = max(ans, dp[i][j])

    out(str(ans))
                
        
if __name__ == "__main__":
    main()