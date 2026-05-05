from bisect import bisect_left
from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        li = []
        for x in nums[::-1]:
            j = bisect_left(li, x)
            if j == len(li):  # >=x 的 g[j] 不存在
                li.append(x)
            else:
                li[j] = x
        
        pre = []
        length = 0
        for x in nums:
            j = bisect_left(pre, x)
            if j == len(pre):
                pre.append(x)
            else:
                pre[j] = x
            while li and li[-1] <= x:
                li.pop()
            length = max(length, len(pre) + len(li))

        return n - length       # 错误
    

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        suf = [0] * n
        li = []
        for i in range(n - 1, -1, -1):
            x = nums[i]
            j = bisect_left(li, x)
            if j == len(li):
                li.append(x)
            else:
                li[j] = x
            suf[i] = j + 1

        length = 0
        li = []
        for i, x in enumerate(nums):
            j = bisect_left(li, x)
            if j == len(li):
                li.append(x)
            else:
                li[j] = x
            if 1 < i < n - 1:
                length = max(length, len(li) + suf[i] + 1)
        
        return n - length   # 错误
    

class Solution:
    # 前后缀分解 + LIS
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        suf = [0] * n
        li = []
        for i in range(n - 1, -1, -1):
            x = nums[i]
            j = bisect_left(li, x)
            if j == len(li):
                li.append(x)
            else:
                li[j] = x
            suf[i] = j + 1

        pre = [0] * n
        li = []
        for i in range(n):
            x = nums[i]
            j = bisect_left(li, x)
            if j == len(li):
                li.append(x)
            else:
                li[j] = x
            pre[i] = j + 1

        length = 0
        for i in range(n):
            if pre[i] > 1 and suf[i] > 1:
                length = max(length, pre[i] + suf[i] - 1)        
                
        return n - length