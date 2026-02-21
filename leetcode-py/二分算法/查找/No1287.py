from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    # 注意边界就好
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        m = n // 4 + 1
        for i in range(0,n-m+1):
            if arr[i] == arr[i + m -1]:
                return arr[i] # O(n)

class Solution:
    # 灵神
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        m = n // 4
        for i in (m, m * 2 + 1):
            x = arr[i]
            if bisect_right(arr, x) - bisect_left(arr, x) > m:
                return x
        # 如果答案不是 arr[m] 也不是 arr[2m+1]，那么答案一定是 arr[3m+2]
        return arr[m * 3 + 2] # O(logn)
# 可证明:一般地，我们至多检查 3 个下标 m,2m+1,3m+2，其中一定有一个 arr[i] 的出现次数至少为 m+1