from functools import cache
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def dfs(i:int):
            if i == len(nums):
                return True
            for j in range(k):
                if j and buckets[j] == buckets[j-1]: # 剪枝
                    continue
                buckets[j] += nums[i] # 进桶
                if buckets[j] <= average and dfs(i + 1):
                    return True
                buckets[j] -= nums[i] # 离桶
            return False
        
        total = sum(nums)
        if total % k != 0:
            return False
        average = total // k
        nums.sort(reverse=True) # 倒序排序提高剪枝成功率
        buckets = [0] * k

        return dfs(0) # 11ms

# 以上那个会出现重复选择的情况
# 以下是加入记忆化后的代码 可以使用used = [False] * n 或者采取二进制方式

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        @cache
        def dfs(state:int,temp:int):
            if state == mask:
                return True
            for i,v in enumerate(nums):
                if (state >> i) & 1: # 已经选过
                    continue
                if temp + v > average:
                    break
                if dfs(state | 1 << i,(temp+v)%average):
                    return True
            return False
        total = sum(nums)
        if total % k != 0:
            return False
        average = total // k
        nums.sort(reverse=True) # 排序稍微快一点
        mask = (1 << len(nums)) - 1
        return dfs(0,0) # 但是比上面慢

