from collections import defaultdict
from itertools import accumulate
from math import inf
from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        ans = cur_sum = sum(nums[:k])
        left = 0
        cnt = defaultdict(int)
        for i in range(k - 1):
            cnt[i] = nums[i]
        cnt[k - 1] = cur_sum

        for i in range(k, len(nums)):
            cur_sum += nums[i]
            cur_sum -= nums[left]

            if left >= k - 1 and cnt[left] >= 0:
                cnt[i] = cur_sum + cnt[left]
            else:
                cnt[i] = cur_sum

            if cnt[i] > ans:
                ans = cnt[i]
            left += 1
        return ans  # 263ms 应该先初始化好cnt 内存过高
    

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        ans = cur_sum = sum(nums[:k])

        cnt = [-inf] * k
        cnt[k - 1] = cur_sum

        for i in range(k, len(nums)):
            j = i % k
            cur_sum += nums[i]
            cur_sum -= nums[i - k]

            ans = max(ans, cur_sum, cur_sum + cnt[j])
            cnt[j] = max(cur_sum, cur_sum + cnt[j])
        
        return ans  # 329ms
    
# 对上式子优化
fmax = lambda x, y: x if x > y else y
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        ans = cur_sum = sum(nums[:k])

        cnt = [-inf] * k
        cnt[k - 1] = cur_sum

        for i in range(k, len(nums)):
            j = i % k
            cur_sum += nums[i] - nums[i - k]

            cnt[j] = fmax(cur_sum, cur_sum + cnt[j])
            ans = fmax(ans, cnt[j])
        
        return ans  # 183ms


class Solution:
    # 灵神
    # 前缀和
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        pre = list(accumulate(nums, initial=0))
        min_s = [inf] * k
        ans = -inf
        for j, s in enumerate(pre):
            i = j % k
            ans = max(ans, s - min_s[i])
            min_s[i] = min(min_s[i], s)
        return ans  # 385ms

class Solution:
    # 灵神
    # 前缀和
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        min_s = [inf] * k
        min_s[-1] = s = 0
        ans = -inf
        for j, x in enumerate(nums):
            s += x
            i = j % k
            ans = max(ans, s - min_s[i])
            min_s[i] = min(min_s[i], s)
        return ans  # 372ms