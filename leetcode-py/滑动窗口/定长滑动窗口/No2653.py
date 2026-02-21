from typing import List
from sortedcontainers import SortedList # type: ignore
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        for i in range(k,len(nums)+1):
            target = sorted(nums[i-k:i])[x-1]
            if target > 0:
                target = 0
            res.append(target)
        return res  # 超时
    
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        res = [0] * (len(nums) - k + 2)
        res[0] = 1 # 哨兵
        for i in range(k,len(nums)+1):
            if nums[i-1] > 0 and res[i-k] == 0:
                continue
            else:
                target = sorted(nums[i-k:i])[x-1]
                if target > 0:
                    target = 0
                res[i-k+1] = target
        return res[1:]  # 超时

# 由于值域很小,timsort很浪费时间

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        l = SortedList()
        # 初始化
        for i in range(k-1):
            l.add(nums[i])

        res = []

        for i in range(k-1,len(nums)):
            l.add(nums[i])
            res.append(min(0,l[x-1]))
            l.remove(nums[i-k+1])
        
        return res  # 2420ms

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        l = SortedList()

        res = []
        left = 0
        for right in range(len(nums)):
            # 只对负数处理
            if nums[right] < 0:
                l.add(nums[right])
            # 调整窗口长度
            if right - left + 1 > k : 
                l.discard(nums[left])
                left += 1

            if right - left + 1 == k:
                if len(l) >= x:
                    res.append(l[x-1])
                else:
                    res.append(0)
        return res  # 1439ms
