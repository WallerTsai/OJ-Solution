from collections import deque
from math import inf
from typing import List


class Solution:
    # 灵神 + 正难则反
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # ans = max(没跨界最大数组和， 跨界最大数组和)
        # 其中 跨界最大数组和 = sum - 没跨界最小数组和
        max_f = 0     # 计算最大子数组和的 DP 数组（空间优化成一个变量）
        max_s = -inf  # 最大子数组和，不能为空
        min_f = 0     # 计算最小子数组和的 DP 数组（空间优化成一个变量）
        min_s = 0     # 最小子数组和，可以为空（元素和为 0）

        for x in nums:
            # 53. 最大子数组和（空间优化写法）
            max_f = max(max_f, 0) + x
            max_s = max(max_s, max_f)
            min_f = min(min_f, 0) + x
            min_s = min(min_s, min_f)

        if max_s < 0:
            return max_s
        return max(max_s, sum(nums) - min_s)


class Solution:
    # 倍增 + 队列
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        nums = nums * 2
        ans = -inf
        s = 0
        q = deque()
        q.append((-1, inf))
        for i, x in enumerate(nums):
            while q and q[0][0] < i - n:
                q.popleft()
            s += x
            ans = max(ans, s - q[0][1])
            while q and q[-1][1] >= s:
                q.pop()
            q.append((i, s))
        return ans

