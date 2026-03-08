from typing import List


class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2:
            return [0, 0]
        MAX, MIN = max(nums), min(nums)
        def func(flag: int):
            array = nums.copy()
            res = 0
            for i, x in enumerate(array):
                if (x % 2 == i % 2) == flag:
                    continue
                if x == MAX:
                    array[i] -= 1
                elif x == MIN:
                    array[i] += 1
                res += 1
            return [res, max(array) - min(array)]

        return min(func(0), func(1))
                
            