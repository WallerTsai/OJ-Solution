# s1 = {1, 2, 3, 4}
# s2 = {1, 3, 5, 7}

# print(s1 - s2)


from bisect import bisect_right
from math import inf
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = inf
        nums.sort()
        n = len(nums)
        the_set = set(nums)
        li = sorted(the_set)
        for i in li:
            s1 = set(range(i, i + n))
            length = len(s1 - the_set)
            ans = min(ans, length)
        return ans  # 超时

class Solution:
    # 暴力
    def minOperations(self, nums: List[int]) -> int:
        ans = inf
        n = len(nums)
        the_set = set(nums)
        li = sorted(the_set)
        for i in li:
            s1 = set(range(i, i + n))
            length = len(s1 - the_set)
            ans = min(ans, length)
        return ans  # 超时

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        li = sorted(set(nums))
        ans = left = 0
        for right, x in enumerate(li):
            while li[left] < x - n + 1:
                left += 1
            ans = max(ans, right - left + 1)
        return n - ans

class Solution:
    # 滑动窗口
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        li = sorted(set(nums))
        ans = left = 0
        for right, x in enumerate(li):
            if li[left] < x - n + 1:
                left += 1
            ans = max(ans, right - left + 1)
        return n - ans  # 135ms

class Solution:
    # 二分
    def minOperations(self, nums: List[int]) -> int:
        ans = n = len(nums)
        nums = sorted(set(nums))
        for i, v in enumerate(nums):
            j = bisect_right(nums, v + n - 1)
            ans = min(ans, n - (j - i))
        return ans  # 207ms