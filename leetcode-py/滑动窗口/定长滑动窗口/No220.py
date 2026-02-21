from bisect import bisect_left
from typing import List
from sortedcontainers import SortedList

class Solution:
    # 二分查找
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:

        for index,num in enumerate(nums):
            area = sorted(nums[index+1:index+indexDiff+1])
            second_index = bisect_left(area,num)
            if second_index != 0:
                if abs(area[second_index-1]-num) <= valueDiff:
                    return True
            if second_index != len(area):
                if abs(area[second_index]-num) <= valueDiff:
                    return True
        return False    # 超时
    

class Solution:
    # 二分查找 + 有序列表数据结构
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        sl = SortedList()
        left = 0
        for right,num in enumerate(nums):
            if right - left > indexDiff:
                sl.remove(nums[left])
                left += 1
            index = bisect_left(sl,num)
            if sl:
                if index != 0:
                    if abs(num - sl[index-1]) <= valueDiff:
                        return True
                if index != len(sl):
                    if abs(num - sl[index]) <= valueDiff:
                        return True
            sl.add(num)
        return False    # 3675ms

class Solution:
    # 桶原理(单个)
    # 思路来自leetcode大佬
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
            buckets = {}
            buckets_size = valueDiff + 1

            for i,num in enumerate(nums):
                # 需要放进哪个桶
                bucket_num = num // buckets_size
                # 如果桶已经存在
                if bucket_num in buckets:
                    return True
                # 加入桶
                buckets[bucket_num] = num
                # 检查前一个桶
                if (bucket_num-1) in buckets and num - buckets[bucket_num-1] <= valueDiff:
                    return True
                # 检查后一个桶
                if (bucket_num+1) in buckets and buckets[bucket_num+1] - num <= valueDiff:
                    return True
                # 如果不构成返回条件，那么当i >= k 的时候就要删除旧桶了，以维持桶中的元素索引跟下一个i+1索引只差不超过indexDiff
                if i >= indexDiff:
                    buckets.pop(nums[i-indexDiff]//buckets_size)
            return False    # 170ms

fun = Solution()
outcome = fun.containsNearbyAlmostDuplicate([1,2,3,1],3,0)


