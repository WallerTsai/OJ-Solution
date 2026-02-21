from math import inf
from typing import List


class Solution:
    # 逆向思维：从nums找最长子数组，使得他元素和等于sum - x
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        res = left = temp = 0
        for right,num in enumerate(nums):
            temp += num
            while temp > target:
                temp -= nums[left]
                left += 1
            if temp == target:
                res = max(res,right-left+1)
        
        if res == 0:
            return -1
        
        return len(nums)-res    # 75ms

class Solution:
    # 正向思维
    # 灵神代码
    def minOperations(self, nums: List[int], x: int) -> int:
        s, n = 0, len(nums)
        right = n
        while right and s + nums[right - 1] <= x:  # 计算最长后缀
            right -= 1
            s += nums[right]
        if right == 0 and s < x: return -1  # 全部移除也无法满足要求
        ans = n - right if s == x else inf
        for left, num in enumerate(nums):
            s += num
            while right < n and s > x:  # 缩小后缀长度
                s -= nums[right]
                right += 1
            if s > x: break  # 缩小失败，说明前缀过长
            if s == x: ans = min(ans, left + 1 + n - right)  # 前缀+后缀长度
        return ans if ans <= n else -1