from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            res.append(nums[num])
        return res

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[v] for v in nums]