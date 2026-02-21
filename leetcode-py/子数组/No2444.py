from math import inf
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        minK_index, maxK_index = set(), set()
        for i, num in enumerate(nums):
            if num == minK:
                minK_index.add(i)
            if num == maxK:
                maxK_index.add(i)

        n = len(nums)

        dp = [[0] * n for _ in range(n)]
        ans = 0
        for i in range(n):
            min_flag = False
            max_flag = False
            for j in range(i,n):
                if i in minK_index:
                    min_flag = True
                if i in maxK_index:
                    max_flag = True
                if min_flag and max_flag:
                    ans += n - j
                    break
        return ans  # 错误
    
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            MIN, MAX = inf, -inf
            for j in range(i,n):
                if nums[j] > MAX:
                    MAX = nums[j]
                if nums[j] < MIN:
                    MIN = nums[j]
                if MIN == minK and MAX == maxK:
                    dp[i][j] = 1
                elif MIN < minK or MAX > maxK:
                    break
        
        return sum(k for r in dp for k in r)    # 爆内存
    
class Solution:
    # 暴力
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            MIN, MAX = inf, -inf
            for j in range(i,n):
                if nums[j] > MAX:
                    MAX = nums[j]
                if nums[j] < MIN:
                    MIN = nums[j]
                if MIN == minK and MAX == maxK:
                    ans += 1
                elif MIN < minK or MAX > maxK:
                    break
        
        return ans  # 超时
    
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        min_index = max_index = temp = -1   # 注意这里的 - 1
        for i, x in enumerate(nums):
            if x == minK:
                min_index = i
            if x == maxK:
                max_index = i
            if not minK <= x <= maxK:
                temp = i
            ans += max(min(min_index, max_index) - temp, 0) # 和 temp 相互配合
        return ans