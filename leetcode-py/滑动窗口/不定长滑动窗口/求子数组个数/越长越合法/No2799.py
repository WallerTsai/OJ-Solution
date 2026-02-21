from collections import Counter
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        m = len(set(nums))
        cnt = Counter()
        res = left = 0
        for right,num in enumerate(nums):
            cnt[num] += 1
            while len(cnt) == m:
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    cnt.pop(nums[left])
                left += 1
            res += left
        return res  # 11ms


