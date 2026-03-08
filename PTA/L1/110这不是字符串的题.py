from itertools import pairwise
import sys
# sys.setrecursionlimit(1_000_000_000)

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())

# data = sys.stdin.read().strip().split()
# it = iter(data)

out = sys.stdout.write 

# 暴力模拟
n, m = mii()
s_li = lii()
for _ in range(m):
    n = len(s_li)   # 更新
    flat = ii()
    if flat == 1:
        pattern = lii()
        l, pattern = pattern[0], pattern[1:]
        target = lii()[1:]
        l = len(pattern)
        for i in range(0, n - l + 1):
            if s_li[i: i + l] == pattern:
                s_li[i: i + l] = target
                break
    elif flat == 2:
        new_li = []
        for a, b in pairwise(s_li):
            new_li.append(a)
            if (a + b) % 2 == 0:
                avg = (a + b) // 2
                new_li.append(avg)
        new_li.append(s_li[-1])
        s_li = new_li
    elif flat == 3:
        left, right = mii()
        s_li[left - 1: right] = s_li[left - 1: right][::-1]
print(*s_li)
    


# gemini AC 代码

import sys

def solve():
    # 1. 一次性读取所有数据，完美避开换行和空格的坑
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    
    def next_int():
        return int(next(it))

    n = next_int()
    m = next_int()
    
    # 2. 降维打击：用 bytearray 存储数字，因为数字 <= 26，完全在一个字节范围内
    arr = bytearray(next_int() for _ in range(n))
    
    for _ in range(m):
        op = next_int()
        
        if op == 1:
            l1 = next_int()
            pattern = bytearray(next_int() for _ in range(l1))
            l2 = next_int()
            target = bytearray(next_int() for _ in range(l2))
            
            # bytearray 自带的 replace，底层 C 实现的字符串匹配算法（如 Boyer-Moore）
            # 第三个参数 1 表示“只替换第一次出现的”
            arr = arr.replace(pattern, target, 1)
            
        elif op == 2:
            if len(arr) < 2:
                continue
            new_arr = bytearray()
            # 用 zip 替代 pairwise，避免 Python 版本兼容问题，且速度极快
            for a, b in zip(arr, arr[1:]):
                new_arr.append(a)
                if (a + b) % 2 == 0:
                    new_arr.append((a + b) // 2)
            new_arr.append(arr[-1])
            arr = new_arr
            
        elif op == 3:
            left = next_int()
            right = next_int()
            
            # bytearray 的原地切片翻转也是极快的
            sub = arr[left - 1 : right]
            sub.reverse()
            arr[left - 1 : right] = sub

    # 3. 输出结果
    sys.stdout.write(" ".join(map(str, arr)) + "\n")

if __name__ == '__main__':
    solve()
