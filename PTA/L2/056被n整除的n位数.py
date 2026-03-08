import sys
# sys.setrecursionlimit(1_000_000_000)

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())

# data = sys.stdin.read().strip().split()
# it = iter(data)

out = sys.stdout.write 


n, low, high = mii()
ans = []
pow10 = [10 ** i for i in range(16)]

def dfs(i: int, cur: int):
    if i == n and low <= cur <= high:
        ans.append(cur)
        return
    rem = n - i
    min_val = cur * pow10[rem]
    max_val = min_val + pow10[rem] - 1

    if max_val < low or min_val > high:
        return
    
    start = 1 if i == 0 else 0
    for d in range(start, 10):
        nxt = cur * 10 + d
        if nxt % (i + 1) == 0:
            dfs(i + 1, nxt)

dfs(0, 0)

if ans:
    out('\n'.join(map(str,ans)))
else:
    out("No Solution")



import sys

def main():

    data = sys.stdin.read().split()
    n = int(data[0])
    a = int(data[1])
    b = int(data[2])

    min_limit = max(a, 10 ** (n - 1))
    max_limit = min(b, 10 ** n - 1)

    if min_limit > max_limit:
        sys.stdout.write("No Solution\n")
        return

    s_min = str(min_limit)
    s_max = str(max_limit)

    ans = []

    def dfs(pos, current_val, is_limit_down, is_limit_up):
        if pos == n:
            ans.append(current_val)
            return

        down = int(s_min[pos]) if is_limit_down else (1 if pos == 0 else 0)
        up = int(s_max[pos]) if is_limit_up else 9

        for d in range(down, up + 1):
            next_val = current_val * 10 + d
            if next_val % (pos + 1) == 0:
                dfs(pos + 1, 
                    next_val, 
                    is_limit_down and (d == down), 
                    is_limit_up and (d == up))

    dfs(0, 0, True, True)

    if ans:
        sys.stdout.write('\n'.join(map(str, ans)) + '\n')
    else:
        sys.stdout.write("No Solution\n")

if __name__ == '__main__':
    main()