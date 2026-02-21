from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(key=abs)
        a, b = nums[-1], nums[-2]
        return abs(a) * abs(b) * pow(10,5)  # O(nlogn)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = mx2 = 0
        for x in nums:
            x = abs(x)
            if x > mx:
                mx2 = mx  # 原来的最大变成次大
                mx = x  # x 是新的最大
            elif x > mx2:
                mx2 = x  # 最大不变，x 是新的次大
        return mx * mx2 * 10 ** 5   # O(n)