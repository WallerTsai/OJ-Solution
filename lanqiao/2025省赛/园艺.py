import sys
# sys.setrecursionlimit(1_000_000)

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())
# data = sys.stdin.read().strip().split()
# it = iter(data)
out = sys.stdout.write   
fmax = lambda x, y : x if x > y else y

def main():
    n = ii()
    h = lii()

    ans = 1
    for d in range(1, n):
        # 剪枝
        if ans >= (n - 1) // d + 1:
            break
        
        for start in range(d):
            if ans >= (n - start - 1) // d + 1:
                break
            cur = 1
            for i in range(start + d, n, d):
                if h[i] > h[i - d]:
                    cur += 1
                    ans = fmax(ans, cur)
                else:
                    cur = 1
                    if ans >= (n - i - 1) // d + 1:
                        break

    out(str(ans))

if __name__ == "__main__":
    main()



# dp
import sys
# sys.setrecursionlimit(1_000_000)

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())
# data = sys.stdin.read().strip().split()
# it = iter(data)
out = sys.stdout.write   
fmax = lambda x, y : x if x > y else y

def solve():
    n = ii()
    h = lii()
    
    dp = [[1] * (n + 1) for _ in range(n + 1)]
    ans = 1
    
    for i in range(n):
        for j in range(i):
            if h[j] < h[i]:
                d = i - j
                dp[i][d] = fmax(dp[i][d], dp[j][d] + 1)
                if dp[i][d] > ans:
                    ans = dp[i][d]
                    
    print(ans)

if __name__ == '__main__':
    solve()