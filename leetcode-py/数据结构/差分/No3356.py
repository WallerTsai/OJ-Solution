from itertools import accumulate
from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        def isZeroArray(k: int) -> bool:
                diff = [0] * (len(nums) + 1)
                for l, r, val in queries[:k]:
                    diff[l] += val
                    diff[r + 1] -= val

                for num, d in zip(nums,accumulate(diff)):
                    if num > d:
                        return False
                return True 
        
        n = len(queries)
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if isZeroArray(mid):
                right = mid
            else:
                left = mid + 1
        
        return left if left <= n else -1    # 错误
    
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        def isZeroArray(k: int) -> bool:
                diff = [0] * (len(nums) + 1)
                for l, r, val in queries[:k]:
                    diff[l] += val
                    diff[r + 1] -= val

                for num, d in zip(nums,accumulate(diff)):
                    if num > d:
                        return False
                return True 
        
        n = len(queries)
        left, right = 0, n + 1
        while left < right:
            mid = (left + right) // 2
            if isZeroArray(mid):
                right = mid
            else:
                left = mid + 1
        
        return left if left <= n else -1    # 1027ms
    
class Solution:
    # 三指针
    # 灵神
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        diff = [0] * (len(nums) + 1)
        sum_d = k = 0
        for i, (x, d) in enumerate(zip(nums, diff)):
            sum_d += d
            while k < len(queries) and sum_d < x:  # 需要添加询问，把 x 减小
                l, r, val = queries[k]
                diff[l] += val
                diff[r + 1] -= val
                if l <= i <= r:  # x 在更新范围中
                    sum_d += val
                k += 1
            if sum_d < x:  # 无法更新
                return -1
        return k
    
# 这段代码并没有直接修改迭代对象 nums 或 diff 的长度，而是修改了 diff 的某些元素的值。从这个角度来看，代码的逻辑是合理的，不会导致迭代器失效的问题。
# 为什么这段代码可以正常运行？
# diff 的长度没有改变：虽然代码修改了 diff 的某些元素的值，但 diff 的长度始终保持不变。因此，迭代器仍然可以正常工作。
# 迭代逻辑是独立的：代码中对 diff 的修改是基于索引的，而不是基于迭代器的。diff 的修改不会影响到 nums 或 queries 的迭代逻辑。