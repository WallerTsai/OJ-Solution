from itertools import accumulate


class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        suf_max = list(accumulate(nums[::-1], func=max, initial=0))[::-1]
        res = []
        pre_max = 0
        for i, num in enumerate(nums):
            if num > pre_max or num > suf_max[i + 1]:
                res.append(num)
            pre_max = max(pre_max, num)
        return res