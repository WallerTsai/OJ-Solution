import sys


input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())
out = sys.stdout.write
fmax = lambda x, y : x if x > y else y 
fmin = lambda x, y : x if x < y else y

def main():
    n, c, b = mii()
    s_li = lii()
    a_li = lii()

    dp = [[-1] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = b

    for i in range(1, n + 1):
        s, a = s_li[i - 1], a_li[i - 1]
        for k in range(i + 1):
            # 不在该房间使用增幅
            if dp[i - 1][k] != -1:
                new_s = fmin(dp[i - 1][k] + s, c)
                if new_s >= a:
                    dp[i][k] = fmax(dp[i][k], new_s)
            # 在该房间使用
            if k > 0 and s > 0 and dp[i - 1][k - 1] != -1:
                new_s = fmin(dp[i - 1][k - 1] + 2 * s, c)
                if new_s >= a:
                    dp[i][k] = fmax(dp[i][k], new_s)

    for k in range(n + 1):
        if dp[n][k] != -1:
            out(str(k))
            return
        
    out(str(-1))

if __name__ == "__main__":
    main()
                
# 以上代码炸内存



import sys


input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())
out = sys.stdout.write
fmax = lambda x, y : x if x > y else y 
fmin = lambda x, y : x if x < y else y

def main():
    n, c, b = mii()
    s_li = lii()
    a_li = lii()

    dp = [-1] * (n + 1)
    dp[0] = b

    for i in range(1, n + 1):
        s, a = s_li[i - 1], a_li[i - 1]
        new_dp = [-1] * (n + 1)
        for k in range(i + 1):
            # 不在该房间使用增幅
            if dp[k] != -1:
                new_s = fmin(dp[k] + s, c)
                if new_s >= a:
                    new_dp[k] = fmax(new_dp[k], new_s)
            # 在该房间使用
            if k > 0 and s > 0 and dp[k - 1] != -1:
                new_s = fmin(dp[k - 1] + 2 * s, c)
                if new_s >= a:
                    new_dp[k] = fmax(new_dp[k], new_s)
        dp = new_dp

    for k in range(n + 1):
        if dp[k] != -1:
            out(str(k))
            return
        
    out(str(-1))

if __name__ == "__main__":
    main()



# 他人参考
import sys

it = map(int, sys.stdin.read().split())
n, c, b = next(it), next(it), next(it)
s = [0] + [next(it) for _ in range(n)]
a = [0] + [next(it) for _ in range(n)]
f = [b] + [-1] * n
for i in range(1, n + 1):
    for j in range(n + 1)[::-1]:
        best = -1
        if f[j] != -1:
            if (dpij := min(f[j] + s[i], c)) >= a[i]:
                best = max(best, dpij)
        if j != 0 and f[j - 1] != -1:
            if (dpij := min(f[j - 1] + s[i] * 2, c)) >= a[i]:
                best = max(best, dpij)
        f[j] = best
print(min((j for j in range(n + 1) if f[j] != -1), default=-1))
