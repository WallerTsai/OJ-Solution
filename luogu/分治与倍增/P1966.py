# 数学 + 映射逆序队 + P1908

import sys

sys.setrecursionlimit(200_000)

# f佬的IO模板
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())
out = sys.stdout.write

MOD = 10 ** 8 - 3

temp = []
def msort(array: int, left: int, right: int):
    if right - left <= 1:
        return 0
    
    mid = (left + right) // 2

    res = msort(array, left, mid) + msort(array, mid, right)
    i, j, k = left, mid, left
    
    while i < mid and j < right:
        if array[i] <= array[j]:
            temp[k] = array[i]
            i += 1
        else:
            temp[k] = array[j]
            j += 1
            res += mid - i
            res %= MOD
        k += 1
    
    while i < mid:
        temp[k] = array[i]
        i += 1
        k += 1
    while j < right:
        temp[k] = array[j]
        j += 1
        k += 1
    
    for t in range(left, right):
        array[t] = temp[t]

    return res

if __name__ == "__main__":
    n = ii()
    a = lii()
    b = lii()

    sorted_a = sorted(enumerate(a), key=lambda x: x[1])
    sorted_b = sorted(enumerate(b), key=lambda x: x[1])

    c = [0] * n
    for i in range(n):
        a_ori_idx = sorted_a[i][0]
        b_ori_idx = sorted_b[i][0]
        c[a_ori_idx] = b_ori_idx

    temp = [0] * n
    ans = msort(c, 0, n)
    out(str(ans))


