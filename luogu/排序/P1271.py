def insert_sort(array: list, left: int, right: int):
    for i in range(left + 1, right):
        temp = array[i]
        j = i - 1
        while j >= left and array[j] >= temp:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp
    

def merge(array: list, left: int, mid: int, right: int):
    len1, len2 = mid - left, right - mid
    left_part, right_part = array[left: mid], array[mid: right]

    i, j, k = 0, 0, left

    while i < len1 and j < len2:
        if left_part[i] <= right_part[j]:
            array[k] = left_part[i]
            i += 1
        else:
            array[k] = right_part[j] 
            j += 1
        k += 1
    
    if i < len1:
        array[k:right] = left_part[i:]
    if j < len2:
        array[k:right] = right_part[j:]

def timsort(array):
    n = len(array)
    min_run = 64

    for left in range(0, n, min_run):
        right = min(left + min_run, n)
        insert_sort(array, left, right)

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size
            if mid >= n: break
            right = min(left + 2 * size, n)
            merge(array, left, mid, right)
        size *= 2

import sys

sys.setrecursionlimit(200_000)

# f佬的IO模板
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())
out = sys.stdout.write

if __name__ == "__main__":
    n, m = mii()
    li = lii()
    timsort(li)
    out(' '.join(map(str, li)))
    


# 下面是gemini优化
import sys

# 极速 IO 读取
input = sys.stdin.read

def insert_sort(array, left, right):
    # 插入排序在小数组下依然很快
    for i in range(left + 1, right):
        temp = array[i]
        j = i - 1
        while j >= left and array[j] > temp:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp

def merge(array, temp_arr, left, mid, right):
    len1 = mid - left
    
    # 优化 1：仅将左半边拷贝到辅助数组中
    # 相比于同时切片左右两边，这直接减少了一半的临时内存申请
    temp_arr[0:len1] = array[left:mid]
    
    i = 0           # 指向 temp_arr (左半边)
    j = mid         # 指向 array (右半边)
    k = left        # 指向 array (覆盖位置)
    
    # 优化 2：精简的 while 循环
    while i < len1 and j < right:
        if temp_arr[i] <= array[j]:
            array[k] = temp_arr[i]
            i += 1
        else:
            array[k] = array[j]
            j += 1
        k += 1
        
    # 优化 3：批量覆盖收尾
    # 如果左边没走完，把剩下的批量拍回去。
    # 如果是右边没走完呢？什么都不用做！因为它们已经在 array 的原位了。
    if i < len1:
        remain = len1 - i
        array[k:k + remain] = temp_arr[i:len1]


def timsort(array):
    n = len(array)
    min_run = 64
    
    # 全局唯一辅助数组，彻底解决 PyPy 内存炸裂问题
    # 分配最大可能需要的一半大小（或直接设为 n 防止越界）
    temp_arr = [0] * n

    # 1. 切块进行插入排序
    for left in range(0, n, min_run):
        right = min(left + min_run, n)
        insert_sort(array, left, right)

    # 2. 自底向上合并
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size
            if mid >= n: break
            right = min(left + 2 * size, n)
            # 传入全局 temp_arr
            merge(array, temp_arr, left, mid, right)
        size *= 2

def main():
    # 使用一次性读取，并跳过开头的 n 和 m
    raw_data = input().split()
    if len(raw_data) <= 2: return
    
    # 构建源数组
    nums = [int(x) for x in raw_data[2:]]
    
    timsort(nums)
    
    # 极速输出
    sys.stdout.write(" ".join(map(str, nums)) + "\n")

if __name__ == "__main__":
    main()




import sys
input = sys.stdin.read

def mian():
    data = input().split()
    if not data:
        return
    
    n = int(data[0]) 
    m = int(data[1]) 
    
    counts = [0] * (n + 1)
    
    for i in range(2, len(data)):
        counts[int(data[i])] += 1
    
    res = []
    for i in range(1, n + 1):
        res.extend([str(i)] * counts[i])

    
    sys.stdout.write(" ".join(res))

if __name__ == "__main__":
    mian()