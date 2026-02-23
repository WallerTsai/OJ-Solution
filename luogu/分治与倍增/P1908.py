import sys

sys.setrecursionlimit(200_000)

# f佬的IO模板
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())
out = sys.stdout.write



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
    array = lii()

    temp = [0] * n
    ans = msort(array, 0, n)
    out(str(ans))
    


class NumArray:
    @staticmethod
    def lowbit(x):
        return x & -x
    
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, index: int, value: int) -> None:
        index += 1
        while index <= self.n:
            self.tree[index] += value
            index += self.lowbit(index)

    def query(self, index: int) -> int:
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self.lowbit(index)
        return res
    
    def sumRange(self, left: int, right: int) -> int:
        return self.query(right + 1) - self.query(left)
    
if __name__ == "__main__":
    n = ii()
    array = lii()
    sorted_arr = sorted(set(array))
    _map = {val: i + 1 for i,val in enumerate(sorted_arr)}
    tree = NumArray(n)

    ans = 0
    for i, num in enumerate(array):
        num = _map[num]
        ans += i - tree.query(num)
        tree.add(num, 1)

    out(str(ans))