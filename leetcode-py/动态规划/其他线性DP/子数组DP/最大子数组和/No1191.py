from itertools import accumulate
from math import inf
from typing import List

# 注意 建议在结果后取模

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        def maxSubArray(nums: List[int]) -> int:
            ans = 0
            cur_sum = 0
            for x in nums:
                cur_sum = max(cur_sum, 0) + x
                ans = max(ans, cur_sum)
            return ans

        nums = arr * k
        return maxSubArray(nums) % MOD  # 爆内存

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        def maxSubArray(nums: List[int]) -> int:
            ans = 0
            cur_sum = 0
            for x in nums:
                cur_sum = max(cur_sum, 0) + x
                ans = max(ans, cur_sum)
                print(ans)
            return ans

        if sum(arr) > 0:
            return (sum(arr) * k) % MOD # 这种情况处理方式不对
        
        nums = arr * min(k,2)
        return maxSubArray(nums) % MOD  # 错误，有特殊示例没过
    
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        def maxSubArray(nums: List[int]) -> int:
            ans = 0
            cur_sum = 0
            for x in nums:
                cur_sum = max(cur_sum, 0) + x
                ans = max(ans, cur_sum)
                print(ans)
            return ans

        if sum(arr) > 0:
            return (sum(arr) * k) % MOD # 这种情况处理方式不对
            # 对于这种情况讨论
            # 假设k = 5
            # 那么 arr的后缀最大正值 + sum(arr) * (k - 2) + arr的前缀最大正值

        nums = arr * min(k,2)
        return maxSubArray(nums) % MOD  # 错误，有特殊示例没过
    
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        def maxSubArray(nums: List[int]) -> int:
            ans = 0
            cur_sum = 0
            for x in nums:
                cur_sum = max(cur_sum, 0) + x
                ans = max(ans, cur_sum)
                print(ans)
            return ans

        if sum(arr) > 0:
            pre_MIN = min(min(accumulate(arr)), 0)
            sub_MIN = min(min(accumulate(arr[::-1])), 0)
            return (sum(arr) * k + pre_MIN + sub_MIN) % MOD 

        nums = arr * min(k,2)
        return maxSubArray(nums) % MOD  # 115ms
    # pre_MIN 和 sub_MIN 可以合并， 换思路

class Solution:
    # 53. 最大子数组和
    def maxSubArray(self, nums: List[int]) -> int:
            ans = 0
            cur_sum = 0
            for x in nums:
                cur_sum = max(cur_sum, 0) + x
                ans = max(ans, cur_sum)
                print(ans)
            return ans

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if k == 1:
            return self.maxSubArray(arr)
        ans = self.maxSubArray(arr + arr)   
        ans += max(sum(arr), 0) * (k - 2)
        return ans % 1_000_000_007  # 311ms