import sys
sys.setrecursionlimit(200_000)

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
    
    while i < len1:
        array[k] = left_part[i] 
        i += 1
        k += 1
    while j < len2:
        array[k] = right_part[j]
        j += 1
        k += 1

def timsort(array):
    n = len(array)
    min_run = 32

    for left in range(0, n, min_run):
        right = min(left + min_run, n)
        insert_sort(array, left, right)

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size, n)
            right = min(left + 2 * size, n)
            merge(array, left, mid, right)
        size *= 2

# f佬的IO模板
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())
out = sys.stdout.write 

def main():
    n = ii()
    li = lii()
    timsort(li)
    out(' '.join(map(str, li)))

if __name__ == "__main__":
    main()




import sys
import random
sys.setrecursionlimit(200_000)

def partition(array:list,left:int,right:int)->int:
    # 尝试随机基准值
    rand_idx = random.randint(left, right)
    array[left], array[rand_idx] = array[rand_idx], array[left]

    tmp = array[left]
    while left<right:
        while left<right and array[right] >= tmp:    #从右边找比tmp小的数
            right -= 1                              #right往左走一步
        array[left] = array[right]                    #把右边的值写到左边空位上
        while left<right and array[left] <= tmp:     #从左边找比tmp大的数
            left += 1                               #left往右走一步
        array[right] = array[left]                    #把左边的值写到右边空位上
    array[left] = tmp                                #两箭头重合,tmp归位
    return left

def quick_sort(array:list,left:int,right:int):
    if left<right:
        mid = partition(array,left,right)
        quick_sort(array,left,mid-1)                 #左边递归
        quick_sort(array,mid+1,right)                #右边递归


# f佬的IO模板
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())
out = sys.stdout.write 

if __name__ == "__main__":
    n = ii()
    li = lii()
    random.shuffle(li)
    quick_sort(li, 0, n - 1)
    out(' '.join(map(str, li))) # 超时



import sys
import random

sys.setrecursionlimit(200_000)

def quick_sort_3way(arr: list, left: int, right: int):
    if left >= right:
        return
    
    pivot = arr[random.randint(left, right)]
    
    lt = left      
    gt = right     
    i = left       
    
    while i <= gt:
        if arr[i] < pivot:
            # 如果小于，放到左边，lt和i一起前进
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            # 如果大于，放到右边，gt往左退，但 i 不动
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
        else:
            # 如果等于，直接跳过，留在中间
            i += 1
            
    quick_sort_3way(arr, left, lt - 1)
    quick_sort_3way(arr, gt + 1, right)

# f佬的IO模板
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())
out = sys.stdout.write 

if __name__ == "__main__":
    n = ii()
    li = lii()
    quick_sort_3way(li, 0, n - 1)
    out(' '.join(map(str, li)))