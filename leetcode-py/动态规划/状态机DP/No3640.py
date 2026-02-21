from itertools import pairwise
from math import inf
from typing import List


class Solution:
    # 分组循环
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -inf
        i = 0
        while i < n:
            cnt = 0

            # 第一段
            l = i
            i += 1
            while i < n and nums[i - 1] < nums[i]:
                i += 1
            if i == l + 1 or i == n:
                continue

            # 第二段
            p = i - 1
            cnt += nums[p - 1] + nums[p]
            while i < n and nums[i - 1] > nums[i]:
                cnt += nums[i]  # 第二段必选
                i += 1
            if i == p + 1 or i == n:
                continue

            # 第三段
            q = i - 1
            if nums[i] == nums[q]:
                continue
            cnt += nums[i]  # 必选
            i += 1
            max_s = cur_s = 0
            while i < n and nums[i - 1] < nums[i]:
                cur_s += nums[i]
                max_s = max(max_s, cur_s)
                i += 1
            if i == q + 1:
                continue
            cnt += max_s

            # 第一段掉头
            max_s = cur_s = 0
            for j in range(p - 2, l - 1, -1):
                cur_s += nums[j]
                max_s = max(max_s, cur_s)
            cnt += max_s

            ans = max(ans, cnt)
            i = q

        return ans  # 151ms
    

class Solution:
    # 状态机dp
    # f[i][3] = max(f[i−1][3],f[i−1][2])+nums[i] (nums[i−1]<nums[i])
    # f[i][2] = max(f[i−1][2],f[i−1][1])+nums[i] (nums[i−1]>nums[i])
    # f[i][1] = max(f[i−1][1],nums[i−1])+nums[i] (nums[i−1]<nums[i])
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)

        # f[i][j] 表示以 nums[i] 结尾，且处于状态 j 时的最大子数组和
        # j=0: 第一段上升区间 j=1: 下降区间 j=2: 第二段上升区间
        f = [[-inf] * 3 for _ in range(n)]

        for i in range(1, n):
            pre = nums[i - 1]
            cur = nums[i]

            if pre < cur:
                f[i][0] = max(f[i - 1][0], pre) + cur
                f[i][2] = max(f[i - 1][2], f[i - 1][1]) + cur
            elif pre > cur:
                f[i][1] = max(f[i - 1][1], f[i - 1][0]) + cur

        return max(f[i][2] for i in range(n))   # 423ms
    
# 手写 max 更快
max = lambda a, b: b if b > a else a

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        ans = f1 = f2 = f3 = -inf
        for x, y in pairwise(nums):
            f3 = max(f3, f2) + y if x < y else -inf
            f2 = max(f2, f1) + y if x > y else -inf
            f1 = max(f1, x)  + y if x < y else -inf
            ans = max(ans, f3)
        return ans  # 184ms