from math import inf
import sys

sys.setrecursionlimit(200_000)

# f佬的IO模板
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())
out = sys.stdout.write




if __name__ == '__main__':
    n = ii()
    li = lii()
    
    def func(left: int, right: int):
        if right - left == 1:
            return li[left]
        
        mid = (left + right) // 2

        left_part = func(left, mid)
        right_part = func(mid, right)

        mid2left = mid2right = -inf

        cur = 0
        for i in range(mid - 1, left - 1, -1):
            cur += li[i]
            mid2left = max(mid2left, cur)
        cur = 0
        for i in range(mid, right):
            cur += li[i]
            mid2right = max(mid2right, cur)

        mid_part = mid2left + mid2right

        return max(left_part, mid_part, right_part)
    
    ans = func(0, n)
    out(str(ans))