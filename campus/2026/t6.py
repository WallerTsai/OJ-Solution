import os
import sys
# sys.setrecursionlimit(100_000)

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())

# data = sys.stdin.read().strip().split()
# it = iter(data)

out = sys.stdout.write       


def main():
    MOD = 10 ** 9 + 7
    n, k = mii()
    limits = lii()

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        limit = limits[i - 1]
        for j in range(k + 1):
            for m in range(min(j, limit) + 1):
                dp[i][j] = (dp[i][j] + dp[i-1][j-m]) % MOD

    out(str(dp[n][k]))
    # N * K * K 可能超时

def main():
    MOD = 10 ** 9 + 7
    n, k = mii()
    limits = lii()

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        limit = limits[i - 1]
        pre_sum = [0]
        for j in range(k + 1):
            pre_sum.append((pre_sum[-1] + dp[i - 1][j]) % MOD)
        for j in range(k + 1):
            dp[i][j] = (pre_sum[j + 1] - pre_sum[max(0, j - limit)]) % MOD

    out(str(dp[n][k]))


if __name__ == "__main__":
    main()