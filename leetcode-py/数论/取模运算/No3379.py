from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i, num in enumerate(nums):
            if num > 0:
                nx = (i + num) % n
                result.append(nums[nx])
            elif num < 0:
                nx = (i + num) % n
                result.append(nums[nx])
            else:
                result.append(0)
        return result

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i, num in enumerate(nums):
            if num == 0:
                result.append(0)
            else:
                nx = (i + num) % n
                result.append(nums[nx])

        return result
    
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [nums[(i + x) % n] for i, x in enumerate(nums)]