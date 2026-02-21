
from math import inf
from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        tail = nums2[-1]
        temp = inf
        for i, num in enumerate(nums1):
            if num >= nums2[i]:
                ans += num - nums2[i]
                if nums2[i] <= tail <= num:
                    temp = 0
                else:
                    temp = min(temp,abs(tail - num), abs(tail - nums2[i]))
            else:
                ans += nums2[i] - num
                if num <= tail <= nums2[i]:
                    temp = 0
                else:
                    temp = min(temp,abs(tail - num), abs(tail - nums2[i]))
        return ans + temp + 1



# 手写 min max 更快
min = lambda a, b: b if b < a else a
max = lambda a, b: b if b > a else a

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        target = nums2[-1]
        ans = 1  # 把元素追加到 nums1 的末尾需要一次操作
        mn = inf
        for x, y in zip(nums1, nums2):
            if x > y:
                x, y = y, x  # 保证 x <= y，简化后续逻辑
            ans += y - x
            # 如果 target 在 [x,y] 中，那么在从 x 变成 y 的过程中，可以顺带把 target 追加到 nums1 的末尾，代价为 0
            # 如果 target < x，代价为 x-target
            # 如果 target > y，代价为 target-y
            if mn > 0:  # 如果 target 还不在任何 [x,y] 中，则计算
                mn = min(mn, max(x - target, target - y))
        return ans + max(mn, 0)  # 如果 target 在 [x,y] 中，上面可能会算出负数