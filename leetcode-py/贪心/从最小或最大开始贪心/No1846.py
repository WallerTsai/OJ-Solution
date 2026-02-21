# 难度：中等

from typing import List
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1,len(arr)):
            if arr[i] > arr[i-1] + 1:
                arr[i] = arr[i-1] + 1
        return arr[-1]  # 39ms
    
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        pre = arr[0] = 1
        for i in arr:
            if i > pre + 1:
                i = pre + 1
            pre = i
        return pre  # 22ms