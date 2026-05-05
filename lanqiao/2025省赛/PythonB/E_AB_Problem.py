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
    li = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            li[j] += 1

    pre_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        pre_sum[i] = pre_sum[i - 1] + li[i]

    ans = 0
    for t in range(1, n + 1):
        ans += li[t] * pre_sum[n - t]

    out(str(ans))
        
if __name__ == "__main__":
    main()



def main():
    n = int(input())

    # 先预处理 n 的因数
    l = [0] * (2**20 + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            l[j] += 1
    
    # 前缀和
    pre_l = [0] * (2**20 + 1)
    for i in range(1, n + 1):
        pre_l[i] = pre_l[i - 1] + l[i]

    ans = 0
    for i in range(1, n + 1):
        ans += l[i] * pre_l[n - i]

    print(ans)

main()