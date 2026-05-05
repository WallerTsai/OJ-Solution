from collections import defaultdict
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
    n, k = mii()
    MOD = 10 ** 9 + 7

    if k == 0:
        out(str(pow(2, n, MOD)))
        return
    
    # l_to_cost = defaultdict(int)
    li = [] # [(l, cost)]
    for l in range(n + 1):
        cost = l * (l + 1) // 2
        if cost < k:
            li.append((l, cost))
        else:
            break

    # dp[i][j] 表示长度为 i，结尾是 0，共鸣数为 j 的方案数
    dp = [[0] * k for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for l, c in li:
            pre_i = i - l - 1
            if pre_i < 0:
                break
            for j in range(c, k):
                dp[i][j] = (dp[i][j] + dp[pre_i][j - c]) % MOD

    count = 0
    for l, cost in li:
        i = n - l
        if i > 0:
            for j in range(cost, k):
                count = (count + dp[i][j - cost]) % MOD
        elif i == 0:
            count = (count + 1) % MOD

    ans = (pow(2, n, MOD) - count) % MOD
    out(str(ans))



if __name__ == "__main__":
    main()