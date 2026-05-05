from collections import defaultdict
from itertools import accumulate
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = cnt = left = 0
        for right,num in enumerate(nums):
            cnt += num
            while left < right and cnt > k:
                cnt -= nums[left]
                left += 1
            if cnt == k:
                res += 1
        while left != right:
            cnt -= nums[left]
            if cnt == k:
                res += 1
            left += 1
        return res

# 思考 这道题为什么不可用滑动窗口

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cnt = defaultdict(int)
        for num in accumulate(nums,initial=0):
            res += cnt[num-k]
            cnt[num] += 1
        return res

# 一次遍历
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = s = 0
        cnt = defaultdict(int)
        cnt[0] = 1  # s[0]=0 单独统计
        for x in nums:
            s += x
            ans += cnt[s - k]
            cnt[s] += 1
        return ans
    


# 2026年4月14日
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = pre_sum = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        for x in nums:
            pre_sum += x
            ans += cnt[pre_sum - k]
            cnt[pre_sum] += 1
        return ans



