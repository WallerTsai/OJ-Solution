from itertools import accumulate
from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i, num1 in enumerate(nums):
            for j in range(i + 1, n):
                num = abs(num1 - nums[j])
                result[i] += num
                result[j] += num
        return result   # 超时


# 应该注意到数组有序
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        result = []
        pre_sum = list(accumulate(nums, initial=0))
        n = len(nums)
        print(pre_sum)
        for i, num in enumerate(nums):
            left = i * num - pre_sum[i]
            right = pre_sum[n] - pre_sum[i] - (n - i) * num
            result.append(right + left)
        
        return result

