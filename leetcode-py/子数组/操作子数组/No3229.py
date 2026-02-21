from itertools import pairwise
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        diff = [t - n for n, t in zip(nums, target)]
        ans = abs(diff[0])
        for a, b in pairwise(diff):
            if a ^ b < 0:
                ans += abs(b)
                continue
            if abs(b) > abs(a):
                ans += abs(b) - abs(a)
        return ans  # 91ms
    


class Solution:
    # 灵神
    # https://leetcode.cn/problems/minimum-operations-to-make-array-equal-to-target/solutions/2851722/chai-fen-shu-zu-fen-lei-tao-lun-pythonja-f8lo/
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        pos_sum = neg_sum = 0
        d = target[0] - nums[0]
        if d > 0:
            pos_sum = d
        else:
            neg_sum = -d
        for (n1, t1), (n2, t2) in pairwise(zip(nums, target)):
            d = (t2 - n2) - (t1 - n1)
            if d > 0:
                pos_sum += d
            else:
                neg_sum -= d
        return max(pos_sum, neg_sum)


class Solution:
    # leetcode 大佬
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        t, s = 0, 0
        for x, y in zip(nums, target):
            x -= y
            if x > t:
                s += x - t
            t = x
        return s if x >= 0 else s - x   # 40ms